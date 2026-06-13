from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.index, name='books'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/', views.show_book, name='show_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/update/', views.update_book, name='update_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('books/<int:book_id>/fav/', views.favorite, name='favorite'),
    path('books/<int:book_id>/unfav/', views.unfavorite, name='unfavorite'),
    # SENSEI BONUS
    path('my_books/', views.my_books, name='my_books'),
]