from django.urls import path
from . import views

urlpatterns = [
    path('shows/', views.index, name='index'),
    path('shows/new/', views.new, name='new'),
    path('shows/create/', views.create, name='create'),
    path('shows/<int:show_id>/', views.show, name='show'),
    path('shows/<int:show_id>/edit/', views.edit, name='edit'),
    path('shows/<int:show_id>/update/', views.update, name='update'),
    path('shows/<int:show_id>/destroy/', views.destroy, name='destroy'),
]