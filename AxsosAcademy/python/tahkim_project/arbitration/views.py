from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Case, Booking
from .forms import CaseForm, BookingForm
from .translations import TRANSLATIONS
from . import paypal_utils


def _lang(request):
    lang = request.session.get("site_lang", "ar")
    return lang if lang in TRANSLATIONS else "ar"


def set_language_view(request, lang):
    if lang not in ("ar", "en"):
        lang = "ar"
    request.session["site_lang"] = lang
    next_url = request.META.get("HTTP_REFERER") or "/"
    return redirect(next_url)


def home(request):
    return render(request, "arbitration/home.html")


def ask_case(request):
    lang = _lang(request)
    if request.method == "POST":
        form = CaseForm(request.POST, lang=lang)
        if form.is_valid():
            form.save()
            success_msg = (
                "تم إرسال قضيتك بنجاح، سيتم نشر الحكم قريباً في صفحة القضايا والأحكام."
                if lang == "ar"
                else "Your case was submitted successfully. The ruling will be published soon on the Cases & Rulings page."
            )
            messages.success(request, success_msg)
            return redirect("ask_case")
    else:
        form = CaseForm(lang=lang)
    return render(request, "arbitration/ask.html", {"form": form})


def qa_list(request):
    cases = Case.objects.filter(status="answered").order_by("-answered_at")
    return render(request, "arbitration/qa.html", {"cases": cases})


def booking(request):
    lang = _lang(request)
    if request.method == "POST":
        form = BookingForm(request.POST, lang=lang)
        if form.is_valid():
            new_booking = form.save()
            return redirect("confirm_booking", pk=new_booking.pk)
    else:
        form = BookingForm(lang=lang)
    return render(request, "arbitration/booking.html", {"form": form})


def confirm_booking(request, pk):
    booking_obj = get_object_or_404(Booking, pk=pk)
    confirm_url = request.build_absolute_uri()
    return render(
        request,
        "arbitration/confirm.html",
        {"booking": booking_obj, "confirm_url": confirm_url},
    )


@require_POST
def paypal_create_order(request, pk):
    """يُستدعى من زر PayPal بالمتصفح لإنشاء طلب دفع جديد مرتبط برقم الحجز."""
    booking_obj = get_object_or_404(Booking, pk=pk)
    try:
        order = paypal_utils.create_order(booking_obj)
        return JsonResponse({"id": order["id"]})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@require_POST
def paypal_capture_order(request, order_id):
    """
    يُستدعى بعد موافقة الزائر على الدفع بصفحة PayPal، يلتقط الدفعة فعلياً،
    ثم يقرأ custom_id (رقم الحجز) ويحدّث حالة الدفع تلقائياً بدون تدخل يدوي.
    """
    try:
        result = paypal_utils.capture_order(order_id)
        custom_id = None
        try:
            custom_id = result["purchase_units"][0]["payments"]["captures"][0]["custom_id"]
        except (KeyError, IndexError):
            pass
        if custom_id:
            try:
                booking_obj = Booking.objects.get(pk=custom_id)
                booking_obj.paid = True
                booking_obj.save()  # يستخدم save() عمداً (وليس update()) لتفعيل إشعار البريد تلقائياً
            except Booking.DoesNotExist:
                pass
        return JsonResponse({"status": result.get("status"), "booking_id": custom_id})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
