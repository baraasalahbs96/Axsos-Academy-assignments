from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, Author, Review
from login_app.models import User

def index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    # أحدث 3 ريفيوز
    recent_reviews = Review.objects.all().order_by('-created_at')[:3]
    # باقي الكتب اللي عندها ريفيوز
    recent_book_ids = [r.book.id for r in recent_reviews]
    other_books = Book.objects.filter(
        reviews__isnull=False
    ).exclude(
        id__in=recent_book_ids
    ).distinct()
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'recent_reviews': recent_reviews,
        'other_books': other_books,
    }
    return render(request, 'books_app/index.html', context)

def add_book(request):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == 'GET':
        authors = Author.objects.all()
        return render(request, 'books_app/add_book.html', {'authors': authors})
    
    # Validation
    errors = {}
    if len(request.POST['title'].strip()) == 0:
        errors['title'] = "Title is required."
    if errors:
        for val in errors.values():
            messages.error(request, val)
        return redirect('/books/add/')
    
    # Author: اختر من القائمة أو أضف جديد
    if request.POST.get('new_author') and len(request.POST['new_author'].strip()) > 0:
        author, _ = Author.objects.get_or_create(name=request.POST['new_author'].strip())
    else:
        author = Author.objects.get(id=request.POST['author_id'])
    
    book = Book.objects.create(
        title  = request.POST['title'],
        author = author,
    )
    # إضافة الريفيو مع الكتاب
    if len(request.POST['review'].strip()) > 0:
        Review.objects.create(
            review = request.POST['review'],
            rating = int(request.POST['rating']),
            user   = User.objects.get(id=request.session['user_id']),
            book   = book,
        )
    return redirect(f'/books/{book.id}/')

def show_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    book = Book.objects.get(id=book_id)
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'book': book,
        'reviews': book.reviews.all().order_by('created_at'),
    }
    return render(request, 'books_app/show_book.html', context)

def add_review(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method != 'POST':
        return redirect(f'/books/{book_id}/')
    if len(request.POST['review'].strip()) == 0:
        messages.error(request, "Review cannot be empty.")
        return redirect(f'/books/{book_id}/')
    Review.objects.create(
        review = request.POST['review'],
        rating = int(request.POST['rating']),
        user   = User.objects.get(id=request.session['user_id']),
        book   = Book.objects.get(id=book_id),
    )
    return redirect(f'/books/{book_id}/')

def delete_review(request, review_id):
    if 'user_id' not in request.session:
        return redirect('/')
    review = Review.objects.get(id=review_id)
    book_id = review.book.id
    if review.user.id == request.session['user_id']:
        review.delete()
    return redirect(f'/books/{book_id}/')

def user_profile(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/')
    profile_user = User.objects.get(id=user_id)
    # الكتب اللي كتب عنها الشخص ريفيو
    reviewed_books = Book.objects.filter(
        reviews__user=profile_user
    ).distinct()
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'profile_user': profile_user,
        'reviewed_books': reviewed_books,
        'total_reviews': profile_user.reviews.count(),
    }
    return render(request, 'books_app/user_profile.html', context)