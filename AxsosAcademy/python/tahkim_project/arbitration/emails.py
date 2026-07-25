"""
دوال إرسال رسائل البريد الإلكتروني (تأكيد الحجز، تأكيد الدفع، إشعار المحكّم).
تُستخدم من داخل signals.py تلقائياً، فلا حاجة لاستدعائها يدوياً من العروض (views).
"""
from django.core.mail import send_mail
from django.conf import settings


def send_booking_confirmation_email(booking):
    """يرسل للزائر تأكيداً فورياً بمجرد إنشاء الحجز."""
    if not booking.email:
        return
    subject = "تأكيد استلام حجزك - دار التحكيم الشرعي"
    message = (
        f"مرحباً {booking.name}،\n\n"
        f"تم استلام طلب حجزك بنجاح بالتفاصيل التالية:\n"
        f"- الموضوع: {booking.topic}\n"
        f"- التاريخ: {booking.date}\n"
        f"- الوقت: {booking.time}\n\n"
        f"سيتواصل معك المحكّم قريباً لتأكيد الموعد النهائي.\n\n"
        f"دار التحكيم الشرعي"
    )
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [booking.email], fail_silently=True)


def send_payment_confirmation_email(booking):
    """يرسل للزائر تأكيداً بمجرد أن تتحول حالة الدفع إلى 'مدفوع'."""
    if not booking.email:
        return
    subject = "تأكيد استلام الدفع - دار التحكيم الشرعي"
    message = (
        f"مرحباً {booking.name}،\n\n"
        f"تم تأكيد استلام دفعتك بنجاح لجلسة التحكيم بتاريخ {booking.date} "
        f"الساعة {booking.time}.\n\n"
        f"شكراً لثقتك بدار التحكيم الشرعي."
    )
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [booking.email], fail_silently=True)


def notify_arbitrator_new_booking(booking):
    """يرسل إشعاراً للمحكّم (إن كان بريده مضبوطاً بالإعدادات) بأي حجز جديد."""
    if not settings.ARBITRATOR_EMAIL:
        return
    subject = f"حجز جديد رقم #{booking.pk}"
    message = (
        f"وصل حجز جديد على الموقع:\n\n"
        f"- الاسم: {booking.name}\n"
        f"- الهاتف: {booking.phone}\n"
        f"- البريد: {booking.email or 'غير متوفر'}\n"
        f"- الموضوع: {booking.topic}\n"
        f"- التاريخ: {booking.date} - {booking.time}\n"
    )
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.ARBITRATOR_EMAIL], fail_silently=True)
