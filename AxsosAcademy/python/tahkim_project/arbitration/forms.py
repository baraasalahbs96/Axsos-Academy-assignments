from django import forms
from .models import Case, Booking, CATEGORY_CHOICES
from .translations import CATEGORY_TRANSLATIONS_EN


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ["name", "category", "question"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "مثال: أبو محمد"}),
            "question": forms.Textarea(attrs={"rows": 6, "placeholder": "اشرح تفاصيل النزاع أو القضية بوضوح هنا…"}),
        }
        labels = {
            "name": "الاسم (اختياري، ولن يُنشر مع الحكم)",
            "category": "نوع القضية",
            "question": "تفاصيل القضية",
        }

    def __init__(self, *args, lang="ar", **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].initial = ""  # لا تعرض القيمة الافتراضية "غير محدد" داخل الحقل نفسه
        if lang == "en":
            self.fields["category"].choices = [
                (value, CATEGORY_TRANSLATIONS_EN.get(label, label))
                for value, label in CATEGORY_CHOICES
            ]
            self.fields["name"].label = "Name (optional, won't be published with the ruling)"
            self.fields["category"].label = "Case Type"
            self.fields["question"].label = "Case Details"
            self.fields["name"].widget.attrs["placeholder"] = "e.g. John Doe"
            self.fields["question"].widget.attrs["placeholder"] = "Explain the dispute or case in detail here…"

    def clean_name(self):
        return self.cleaned_data.get("name") or "غير محدد"


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["name", "phone", "email", "topic", "date", "time", "payment_method"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
            "phone": forms.TextInput(attrs={"placeholder": "05xxxxxxxx"}),
            "email": forms.EmailInput(attrs={"placeholder": "example@email.com"}),
        }
        labels = {
            "name": "الاسم",
            "phone": "رقم الهاتف",
            "email": "البريد الإلكتروني (لإرسال تأكيد الحجز والدفع)",
            "topic": "موضوع الاستشارة",
            "date": "التاريخ",
            "time": "الوقت",
            "payment_method": "طريقة الدفع",
        }

    def __init__(self, *args, lang="ar", **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True
        if lang == "en":
            self.fields["name"].label = "Name"
            self.fields["phone"].label = "Phone Number"
            self.fields["email"].label = "Email (for booking & payment confirmation)"
            self.fields["topic"].label = "Consultation Topic"
            self.fields["date"].label = "Date"
            self.fields["time"].label = "Time"
            self.fields["payment_method"].label = "Payment Method"
            self.fields["payment_method"].choices = [
                ("whatsapp", "Pay via WhatsApp"),
                ("online", "Online Payment"),
            ]
