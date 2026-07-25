from django.contrib import admin
from .models import Case, Booking


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ("category", "short_question", "status", "created_at", "answered_at")
    list_filter = ("status", "category")
    search_fields = ("question", "answer", "name")
    readonly_fields = ("created_at", "answered_at")
    fields = ("name", "category", "question", "answer", "status", "created_at", "answered_at")

    @admin.display(description="القضية")
    def short_question(self, obj):
        return obj.question[:60] + ("…" if len(obj.question) > 60 else "")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "topic", "date", "time", "status", "paid", "payment_method")
    list_filter = ("status", "paid", "payment_method")
    search_fields = ("name", "phone", "topic")
    list_editable = ("status", "paid")
    readonly_fields = ("created_at",)
