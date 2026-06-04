from django.shortcuts import render, redirect
import random

def index(request):
    # إذا ما في رقم في الـ session، اختار رقم جديد
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
        request.session['attempts'] = 0
    
    return render(request, 'index.html')

def guess(request):
    user_guess = int(request.POST['guess'])
    secret = request.session['number']
    request.session['attempts'] += 1
    attempts = request.session['attempts']
    
    if user_guess < secret:
        result = 'low'
        message = 'Too low!'
    elif user_guess > secret:
        result = 'high'
        message = 'Too high!'
    else:
        result = 'correct'
        message = f'{secret} was the number!'
    
    context = {
        'message': message,
        'result': result,
        'attempts': attempts,
        'secret': secret,
    }
    return render(request, 'index.html', context)

def play_again(request):
    del request.session['number']
    del request.session['attempts']
    return redirect('/')