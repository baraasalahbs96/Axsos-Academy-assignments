from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_book/', views.create_book),
    path('books/<int:book_id>/', views.view_book),
    path('books/<int:book_id>/add-author/', views.add_author_to_book),
    path('create_author/', views.create_author),
    path('authors/<int:author_id>/', views.view_author),
    path('authors/<int:author_id>/add-book/', views.add_book_to_author),
]