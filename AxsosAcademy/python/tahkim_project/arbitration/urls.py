from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("ask/", views.ask_case, name="ask_case"),
    path("qa/", views.qa_list, name="qa_list"),
    path("booking/", views.booking, name="booking"),
    path("confirm/<int:pk>/", views.confirm_booking, name="confirm_booking"),
    path("set-lang/<str:lang>/", views.set_language_view, name="set_language"),
    path("paypal/create-order/<int:pk>/", views.paypal_create_order, name="paypal_create_order"),
    path("paypal/capture-order/<str:order_id>/", views.paypal_capture_order, name="paypal_capture_order"),
]
