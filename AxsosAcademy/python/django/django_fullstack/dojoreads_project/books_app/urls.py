from django.urls import path
from . import views

urlpatterns = [
    path('books/',                          views.index,         name='books'),
    path('books/add/',                      views.add_book,      name='add_book'),
    path('books/<int:book_id>/',            views.show_book,     name='show_book'),
    path('books/<int:book_id>/review/',     views.add_review,    name='add_review'),
    path('reviews/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('users/<int:user_id>/',            views.user_profile,  name='user_profile'),
]