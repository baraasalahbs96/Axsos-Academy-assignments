from django.urls import path
from . import views

urlpatterns = [
    path('wall/', views.wall, name='wall'),
    path('post_message/', views.post_message, name='post_message'),
    path('post_comment/<int:msg_id>/', views.post_comment, name='post_comment'),
    path('delete/<int:msg_id>/', views.delete_message, name='delete_message'),
]