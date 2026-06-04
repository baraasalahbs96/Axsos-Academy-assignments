from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('destroy_session', views.destroy_session),
    path('increment_two', views.increment_by_two),  # NINJA BONUS: +2
]