from django.shortcuts import render, redirect

def index(request):
    # إذا ما في session، ابدأ من 0
    if 'counter' not in request.session:
        request.session['counter'] = 0
    
    # زد العداد كل مرة تفتح الصفحة
    request.session['counter'] += 1
    
    context = {
        'count': request.session['counter']
    }
    return render(request, 'index.html', context)

def destroy_session(request):
    del request.session['counter']
    return redirect('/')

#  +2 
def increment_by_two(request):
    request.session['counter'] += 2
    return redirect('/')
