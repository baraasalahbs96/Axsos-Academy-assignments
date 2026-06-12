from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/create/', views.create, name='create'),
    path('courses/destroy/<int:course_id>/', views.destroy_confirm, name='destroy_confirm'),
    path('courses/delete/<int:course_id>/', views.destroy, name='destroy'),
]