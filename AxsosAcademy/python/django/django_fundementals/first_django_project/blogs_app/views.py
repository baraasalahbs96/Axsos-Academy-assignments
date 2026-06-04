# blogs_app/views.py
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse

# / → redirect to /blogs
def root(request):
    return redirect('/blogs')

# /blogs
def index(request):
    return HttpResponse("display a list of all blogs")

# /blogs/new
def new(request):
    return HttpResponse("display a new form to create a new blog")

# /blogs/create → redirect to /
def create(request):
    return redirect('/')

# /blogs/<number>
def show(request, number):
    return HttpResponse(f"display blog number: {number}")

# /blogs/<number>/edit
def edit(request, number):
    return HttpResponse(f"display form to edit blog {number}")

# /blogs/<number>/delete → redirect to /blogs
def destroy(request, number):
    return redirect('/blogs')

# BONUS: /blogs/json
def blogs_json(request):
    data = {
        "title": "My first blog",
        "content": "my first blog post"
    }
    return JsonResponse(data)