from django.shortcuts import redirect
from django.http import HttpResponse

def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse("display a list of all blogs")

def new(request):
    return HttpResponse("display a new form to create a new blog")

def create(request):
    return redirect('/blogs')

def show(request, number):
    return HttpResponse(f"display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"display form to edit blog {number}")

def destroy(request, number):
    return redirect('/blogs')