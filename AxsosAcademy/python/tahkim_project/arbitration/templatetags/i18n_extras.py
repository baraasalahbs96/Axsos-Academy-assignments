from django import template
from ..translations import CATEGORY_TRANSLATIONS_EN, BOOKING_STATUS_TRANSLATIONS_EN

register = template.Library()


@register.simple_tag(takes_context=True)
def category_label(context, category_ar):
    """يعرض اسم التصنيف بالعربي أو الإنجليزي حسب لغة الواجهة الحالية."""
    lang = context.get("current_lang", "ar")
    if lang == "en":
        return CATEGORY_TRANSLATIONS_EN.get(category_ar, category_ar)
    return category_ar


@register.simple_tag(takes_context=True)
def status_label(context, status_ar):
    """يعرض حالة الحجز بالعربي أو الإنجليزي حسب لغة الواجهة الحالية."""
    lang = context.get("current_lang", "ar")
    if lang == "en":
        return BOOKING_STATUS_TRANSLATIONS_EN.get(status_ar, status_ar)
    return status_ar
