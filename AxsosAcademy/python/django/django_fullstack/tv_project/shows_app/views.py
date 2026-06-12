from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from .models import Show

# ── Validation ──────────────────────────────────────────
def validate_show(data, show_id=None):
    errors = {}
    title        = data.get('title', '').strip()
    network      = data.get('network', '').strip()
    release_date = data.get('release_date', '').strip()
    description  = data.get('description', '').strip()

    # Title
    if not title:
        errors['title'] = 'Title is required'
    elif len(title) < 2:
        errors['title'] = 'Title must be at least 2 characters'
    else:
        qs = Show.objects.filter(title=title)
        if show_id:
            qs = qs.exclude(id=show_id)
        if qs.exists():
            errors['title'] = 'A show with this title already exists'

    # Network
    if not network:
        errors['network'] = 'Network is required'
    elif len(network) < 3:
        errors['network'] = 'Network must be at least 3 characters'

    # Release Date
    if not release_date:
        errors['release_date'] = 'Release date is required'
    else:
        try:
            rd = date.fromisoformat(release_date)
            if rd >= date.today():
                errors['release_date'] = 'Release date must be in the past'
        except ValueError:
            errors['release_date'] = 'Invalid date format'

    # Description (اختياري، بس إذا موجود 10+)
    if description and len(description) < 10:
        errors['description'] = 'Description must be at least 10 characters'

    return errors

# ── Views ───────────────────────────────────────────────
def index(request):
    all_shows = Show.objects.all()
    return render(request, 'index.html', {'shows': all_shows})

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method != 'POST':
        return redirect('new')

    errors = validate_show(request.POST)
    if errors:
        return render(request, 'new.html', {
            'errors': errors,
            'data': request.POST
        })

    show = Show.objects.create(
        title=request.POST['title'].strip(),
        network=request.POST['network'].strip(),
        release_date=request.POST['release_date'],
        description=request.POST.get('description', '').strip()
    )
    return redirect('show', show_id=show.id)

def show(request, show_id):
    one_show = get_object_or_404(Show, id=show_id)
    return render(request, 'show.html', {'show': one_show})

def edit(request, show_id):
    one_show = get_object_or_404(Show, id=show_id)
    return render(request, 'edit.html', {'show': one_show})

def update(request, show_id):
    if request.method != 'POST':
        return redirect('edit', show_id=show_id)

    one_show = get_object_or_404(Show, id=show_id)
    errors = validate_show(request.POST, show_id=show_id)
    if errors:
        return render(request, 'edit.html', {
            'errors': errors,
            'show': one_show,
            'data': request.POST
        })
    one_show.title = request.POST['title'].strip()
    one_show.network = request.POST['network'].strip()
    one_show.release_date = request.POST['release_date']
    one_show.description = request.POST.get('description', '').strip()
    one_show.save()
    return redirect('show', show_id=one_show.id)

def destroy(request, show_id):
    one_show = get_object_or_404(Show, id=show_id)
    one_show.delete()
    return redirect('index')