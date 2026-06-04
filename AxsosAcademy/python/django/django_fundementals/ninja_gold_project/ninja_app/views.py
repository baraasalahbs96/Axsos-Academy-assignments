from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    
    context = {
        'gold': request.session['gold'],
        'activities': request.session['activities'],
    }
    return render(request, 'index.html', context)

def process_money(request):
    location = request.POST['location']
    now = datetime.now().strftime("%B %d %Y %I:%M %p")
    
    if location == 'farm':
        earned = random.randint(10, 20)
        request.session['gold'] += earned
        msg = f'You entered a farm and earned {earned} gold. ({now})'
        color = 'green'
    elif location == 'cave':
        earned = random.randint(10, 20)
        request.session['gold'] += earned
        msg = f'You entered a cave and earned {earned} gold. ({now})'
        color = 'green'
    elif location == 'house':
        earned = random.randint(10, 20)
        request.session['gold'] += earned
        msg = f'You entered a house and earned {earned} gold. ({now})'
        color = 'green'
    elif location == 'quest':
        amount = random.randint(0, 50)
        win = random.choice([True, False])
        if win:
            request.session['gold'] += amount
            msg = f'You completed a quest and earned {amount} gold. ({now})'
            color = 'green'
        else:
            request.session['gold'] -= amount
            msg = f'You failed a quest and lost {amount} gold. Ouch. ({now})'
            color = 'red'
    
    # أضف النشاط للقائمة
    activities = request.session['activities']
    activities.insert(0, {'msg': msg, 'color': color})
    request.session['activities'] = activities
    
    return redirect('/')

def reset(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return redirect('/')