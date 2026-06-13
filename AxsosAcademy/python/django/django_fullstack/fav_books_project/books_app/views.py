from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book
from login_app.models import User

def index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
        'all_books': Book.objects.all(),
        'my_favs': user.liked_books.all(),
    }
    return render(request, 'books_app/index.html', context)

def add_book(request):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method != 'POST':
        return redirect('/books')
    errors = Book.objects.book_validator(request.POST)
    if errors:
        for val in errors.values():
            messages.error(request, val)
        return redirect('/books')
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.create(
        title       = request.POST['title'],
        desc        = request.POST['desc'],
        uploaded_by = user,
    )
    # كتب رفعها اليوزر تنضاف تلقائياً لـ favorites
    book.users_who_like.add(user)
    return redirect('/books')

def show_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)
    context = {
        'user': user,
        'book': book,
        'likers': book.users_who_like.all(),
        'already_liked': book.users_who_like.filter(id=user.id).exists(),
        'is_owner': book.uploaded_by.id == user.id,
    }
    return render(request, 'books_app/show.html', context)

def edit_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    book = Book.objects.get(id=book_id)
    if book.uploaded_by.id != request.session['user_id']:
        return redirect(f'/books/{book_id}')
    return render(request, 'books_app/edit.html', {'book': book})

def update_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method != 'POST':
        return redirect('/books')
    errors = Book.objects.book_validator(request.POST)
    if errors:
        for val in errors.values():
            messages.error(request, val)
        return redirect(f'/books/{book_id}/edit')
    book = Book.objects.get(id=book_id)
    book.title = request.POST['title']
    book.desc  = request.POST['desc']
    book.save()
    return redirect(f'/books/{book_id}')

def delete_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    book = Book.objects.get(id=book_id)
    if book.uploaded_by.id == request.session['user_id']:
        book.delete()
    return redirect('/books')

def favorite(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)
    book.users_who_like.add(user)
    return redirect(f'/books/{book_id}')

def unfavorite(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)
    book.users_who_like.remove(user)
    return redirect(f'/books/{book_id}')

# SENSEI BONUS
def my_books(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
        'fav_books': user.liked_books.all(),
    }
    return render(request, 'books_app/my_books.html', context)