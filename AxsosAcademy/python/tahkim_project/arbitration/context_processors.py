from django.conf import settings
from .translations import TRANSLATIONS, CATEGORY_TRANSLATIONS_EN


def site_settings(request):
    """يجعل رقم الواتساب، بيانات التواصل، ونظام الترجمة متاحة في كل القوالب."""
    lang = request.session.get("site_lang", "ar")
    if lang not in TRANSLATIONS:
        lang = "ar"
    return {
        "WHATSAPP_NUMBER": getattr(settings, "WHATSAPP_NUMBER", ""),
        "STRIPE_PAYMENT_LINK": getattr(settings, "STRIPE_PAYMENT_LINK", ""),
        "PAYPAL_LINK": getattr(settings, "PAYPAL_LINK", ""),
        "PAYPAL_CLIENT_ID": getattr(settings, "PAYPAL_CLIENT_ID", ""),
        "PAYPAL_CURRENCY": getattr(settings, "PAYPAL_CURRENCY", "USD"),
        "CONTACT_PHONE": getattr(settings, "CONTACT_PHONE", ""),
        "CONTACT_EMAIL": getattr(settings, "CONTACT_EMAIL", ""),
        "current_lang": lang,
        "T": TRANSLATIONS[lang],
        "CATEGORY_TRANSLATIONS_EN": CATEGORY_TRANSLATIONS_EN,
    }
