from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method != 'POST':
        return redirect('index')
    
    errors = User.objects.register_validator(request.POST)
    
    if errors:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('index')
    
    # Hash password 
    hashed_pw = bcrypt.hashpw(
        request.POST['password'].encode(),
        bcrypt.gensalt()
    ).decode()
    
    # Create user انشاء مستخدم
    user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name  = request.POST['last_name'],
        email      = request.POST['email'],
        password   = hashed_pw,
    )
    
    request.session['user_id']   = user.id
    request.session['user_name'] = user.first_name
    
    messages.success(request, "Registration successful!")
    return redirect('success')

def login(request):
    if request.method != 'POST':
        return redirect('index')
    
    errors = User.objects.login_validator(request.POST)
    
    if errors:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('index')
    
    user = User.objects.filter(email=request.POST['email'])[0]
    request.session['user_id']   = user.id
    request.session['user_name'] = user.first_name
    
    messages.success(request, "Login successful!")
    return redirect('success')

def success(request):
    # Guard: منع الوصول بدون تسجيل دخول
    if 'user_id' not in request.session:
        return redirect('index')
    
    user = User.objects.get(id=request.session['user_id'])
    return render(request, 'success.html', {'user': user})

def logout(request):
    request.session.clear()
    return redirect('index')
