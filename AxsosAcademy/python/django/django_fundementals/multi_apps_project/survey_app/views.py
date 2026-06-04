from django.http import HttpResponse

def index(request):
    return HttpResponse("display all the surveys created.")

def new(request):
    return HttpResponse("display a new form to create a new survey.")
