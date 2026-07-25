from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("arbitration.urls")),
]

admin.site.site_header = "لوحة المحكّم — دار التحكيم الشرعي"
admin.site.site_title = "دار التحكيم الشرعي"
admin.site.index_title = "إدارة القضايا والحجوزات"
