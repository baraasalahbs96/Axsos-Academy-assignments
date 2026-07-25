from django.db import models
from django.utils import timezone


CATEGORY_CHOICES = [
    ("نزاعات تجارية", "نزاعات تجارية"),
    ("خلافات أسرية", "خلافات أسرية"),
    ("عقود ومعاملات", "عقود ومعاملات"),
    ("ميراث وتركات", "ميراث وتركات"),
    ("عام", "عام"),
]

CASE_STATUS_CHOICES = [
    ("pending", "بانتظار الحكم"),
    ("answered", "صدر الحكم"),
]


class Case(models.Model):
    """قضية تحكيم مقدَّمة من زائر، يصدر فيها المحكّم حكماً لاحقاً."""

    name = models.CharField("الاسم", max_length=150, blank=True, default="غير محدد")
    category = models.CharField("نوع القضية", max_length=50, choices=CATEGORY_CHOICES, default="عام")
    question = models.TextField("تفاصيل القضية")
    answer = models.TextField("نص الحكم", blank=True, null=True)
    status = models.CharField("الحالة", max_length=20, choices=CASE_STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField("تاريخ التقديم", auto_now_add=True)
    answered_at = models.DateTimeField("تاريخ صدور الحكم", blank=True, null=True)

    class Meta:
        verbose_name = "قضية"
        verbose_name_plural = "القضايا والأحكام"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.category} — {self.question[:40]}"

    def save(self, *args, **kwargs):
        # عند نشر الحكم لأول مرة، سجّل تاريخ الصدور تلقائياً
        if self.status == "answered" and not self.answered_at:
            self.answered_at = timezone.now()
        super().save(*args, **kwargs)


PAYMENT_METHOD_CHOICES = [
    ("whatsapp", "الدفع عبر واتساب"),
    ("online", "الدفع الإلكتروني"),
]

BOOKING_STATUS_CHOICES = [
    ("pending", "بانتظار التأكيد"),
    ("confirmed", "مؤكد"),
    ("cancelled", "ملغي"),
]


class Booking(models.Model):
    """حجز جلسة تحكيم خاصة."""

    name = models.CharField("الاسم", max_length=150)
    phone = models.CharField("رقم الهاتف", max_length=30)
    email = models.EmailField("البريد الإلكتروني", blank=True, default="")
    topic = models.CharField("موضوع الاستشارة", max_length=200)
    date = models.DateField("تاريخ الجلسة")
    time = models.TimeField("وقت الجلسة")
    payment_method = models.CharField("طريقة الدفع", max_length=20, choices=PAYMENT_METHOD_CHOICES, default="whatsapp")
    status = models.CharField("حالة الحجز", max_length=20, choices=BOOKING_STATUS_CHOICES, default="pending")
    paid = models.BooleanField("مدفوع؟", default=False)
    created_at = models.DateTimeField("تاريخ الحجز", auto_now_add=True)

    class Meta:
        verbose_name = "حجز"
        verbose_name_plural = "الحجوزات"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.date} {self.time}"
