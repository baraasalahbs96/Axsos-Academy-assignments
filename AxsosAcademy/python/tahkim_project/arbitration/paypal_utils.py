"""
دوال التعامل مع PayPal REST API (v2 Orders API).
تُستخدم من داخل views.py لإنشاء طلب دفع والتقاطه (تأكيد الدفع الفعلي).
"""
import requests
from django.conf import settings


def _base_url():
    return (
        "https://api-m.sandbox.paypal.com"
        if getattr(settings, "PAYPAL_MODE", "sandbox") == "sandbox"
        else "https://api-m.paypal.com"
    )


def get_access_token():
    """يحصل على توكن وصول مؤقت من PayPal باستخدام Client ID و Secret."""
    resp = requests.post(
        f"{_base_url()}/v1/oauth2/token",
        auth=(settings.PAYPAL_CLIENT_ID, settings.PAYPAL_CLIENT_SECRET),
        data={"grant_type": "client_credentials"},
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json()["access_token"]


def create_order(booking):
    """
    ينشئ طلب دفع جديد على PayPal مرتبط برقم الحجز عبر حقل custom_id،
    وهذا الحقل هو ما يسمح لاحقاً بمطابقة الدفعة بالحجز الصحيح تلقائياً.
    """
    token = get_access_token()
    resp = requests.post(
        f"{_base_url()}/v2/checkout/orders",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        json={
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "custom_id": str(booking.pk),
                    "description": f"جلسة تحكيم - حجز رقم {booking.pk}",
                    "amount": {
                        "currency_code": settings.PAYPAL_CURRENCY,
                        "value": settings.PAYPAL_SESSION_PRICE,
                    },
                }
            ],
        },
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json()


def capture_order(order_id):
    """يلتقط (يؤكد فعلياً) عملية الدفع بعد موافقة الزائر على PayPal."""
    token = get_access_token()
    resp = requests.post(
        f"{_base_url()}/v2/checkout/orders/{order_id}/capture",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json()
