"""
يفرض هذا الوسيط (middleware) اللغة العربية على نصوص Django المدمجة (مثل لوحة
/admin/: "Enabled/Disabled"، "Choose all"...) بغض النظر عن لغة متصفح الزائر،
لأن لوحة الإدارة أداة داخلية للمحكّم ويجب أن تبقى عربية دوماً.
(هذا منفصل تماماً عن مبدّل اللغة عربي/إنجليزي الخاص بواجهة الموقع نفسها،
والذي يعتمد على قاموس الترجمة الخاص بنا في translations.py)
"""
from django.utils import translation


class ForceArabicMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        translation.activate("ar")
        request.LANGUAGE_CODE = "ar"
        response = self.get_response(request)
        translation.deactivate()
        return response
