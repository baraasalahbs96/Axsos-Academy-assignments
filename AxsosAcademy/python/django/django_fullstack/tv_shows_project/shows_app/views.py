from django.shortcuts import render, redirect, get_object_or_404
from .models import Show
from datetime import datetime

def index(request):
    return redirect('/shows/')

def all_shows(request):
    return render(request, 'index.html', {
        'all_shows': Show.objects.all()
    })

def new_show(request):
    return render(request, 'new.html')

def create_show(request):
    if request.method == 'POST':
        show = Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description'],
        )
        return redirect(f'/shows/{show.id}/')
    return redirect('/shows/new/')

def show_detail(request, show_id):
    show = get_object_or_404(Show, id=show_id)
    return render(request, 'show.html', {'show': show})

def edit_show(request, show_id):
    show = get_object_or_404(Show, id=show_id)
    return render(request, 'edit.html', {'show': show})

def update_show(request, show_id):
    if request.method == 'POST':
        show = get_object_or_404(Show, id=show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date'] or None
        show.description = request.POST['description']
        show.save()
        return redirect(f'/shows/{show_id}/')
    return redirect('/shows/')

def destroy_show(request, show_id):
    if request.method == 'POST':
        show = get_object_or_404(Show, id=show_id)
        show.delete()
    return redirect('/shows/')