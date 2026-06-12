from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author

def index(request):
    return render(request, 'index.html', {
        'all_books': Book.objects.all(),
        'all_authors': Author.objects.all(),
    })

def create_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc'],
        )
    return redirect('/')

def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    other_authors = Author.objects.exclude(id__in=book.authors.all())
    return render(request, 'view_book.html', {
        'book': book,
        'other_authors': other_authors,
    })

def add_author_to_book(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        author = get_object_or_404(Author, id=request.POST['author_id'])
        book.authors.add(author)
    return redirect(f'/books/{book_id}/')

def create_author(request):
    if request.method == 'POST':
        Author.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            notes=request.POST['notes'],
        )
    return redirect('/')

def view_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    other_books = Book.objects.exclude(id__in=author.books.all())
    return render(request, 'view_author.html', {
        'author': author,
        'other_books': other_books,
    })

def add_book_to_author(request, author_id):
    if request.method == 'POST':
        author = get_object_or_404(Author, id=author_id)
        book = get_object_or_404(Book, id=request.POST['book_id'])
        author.books.add(book)
    return redirect(f'/authors/{author_id}/')
