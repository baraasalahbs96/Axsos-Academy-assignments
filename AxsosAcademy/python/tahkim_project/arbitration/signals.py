"""
إشارات (Signals) تُرسل البريد الإلكتروني تلقائياً:
- عند إنشاء حجز جديد (تأكيد للزائر + إشعار للمحكّم).
- عند تحوّل حالة الدفع إلى "مدفوع" (سواء تلقائياً عبر PayPal API أو يدوياً من لوحة /admin/).
"""
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Booking
from . import emails


@receiver(post_save, sender=Booking)
def booking_created_notifications(sender, instance, created, **kwargs):
    if created:
        emails.send_booking_confirmation_email(instance)
        emails.notify_arbitrator_new_booking(instance)


@receiver(pre_save, sender=Booking)
def booking_payment_confirmation(sender, instance, **kwargs):
    if not instance.pk:
        return  # حجز جديد لم يُحفظ بعد، سيُعالج عبر post_save أعلاه فقط
    try:
        previous = Booking.objects.get(pk=instance.pk)
    except Booking.DoesNotExist:
        return
    if not previous.paid and instance.paid:
        emails.send_payment_confirmation_email(instance)
