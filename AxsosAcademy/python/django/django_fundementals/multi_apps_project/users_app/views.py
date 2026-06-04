from django.http import HttpResponse

def register(request):
    return HttpResponse("create a new user record.")

def login(request):
    return HttpResponse("users - log in.")

def index(request):
    return HttpResponse("display all the list of users.")