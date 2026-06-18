import bcrypt
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Tree 

def index(request):
    if request.session.get('user_id'):
        return redirect('dashboard')
    return render(request, 'tree_app/index.html')


def register(request):
    if request.method != 'POST':
        return redirect('index')
    errors = User.objects.register_validator(request.POST)
    if errors:
        for key, val in errors.items():
            messages.error(request, val, extra_tags=f'register_{key}')
        return redirect('index')  
    pw_hash = bcrypt.hashpw(
        request.POST['password'].encode(),
        bcrypt.gensalt()
    ).decode()
    user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=pw_hash,
    )
    request.session['user_id'] = user.id
    request.session['user_name'] = user.first_name
    return redirect('dashboard')
    
def login(request):
    if request.method != 'POST':
        return redirect('index')
    errors = User.objects.login_validator(request.POST)
    if errors:
        for key, val in errors.items():
            messages.error(request, val, extra_tags=f'login_{key}')
        return redirect('index')
    
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id']   = user.id
    request.session['user_name'] = user.first_name
    return redirect('dashboard')

def logout(request):
    request.session.flush()
    return redirect('index')

def dashboard(request):
    if not request.session.get('user_id'):
        return redirect('index')
    trees = Tree.objects.select_related('mapped_by').all()
    user_id = request.session['user_id']
    context = {
        'trees': trees,
        'user_id': user_id,
        'user_name': request.session['user_name']
    }
    return render(request, 'tree_app/dashboard.html', context)

def new_tree(request):
    if not request.session.get('user_id'):
        return redirect('index')
    return render(request,'tree_app/new_tree.html', { 'user_name': request.session.get('user_name'), })

def create_tree(request):
    if not request.session.get('user_id'):
        return redirect('index')
    if request.method != 'POST':
        return redirect ('new_tree')
    errors = Tree.objects.create_validator(request.POST)
    if errors:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('new_tree')
    user = User.objects.get(id=request.session['user_id'])
    tree = Tree.objects.create(
        species= request.POST['species'],
        location= request.POST['location'],
        date_found= request.POST['date_found'],
        zip_code= request.POST['zip_code', ''],
        notes= request.POST['notes', ''],
        mapped_by=user
    )
    return redirect('dashboard')

def tree_detail(request, tree_id):
    if not request.session.get('user_id'):
        return redirect('index')
    try:
        tree= Tree.objects.select_related('mapped_by').prefetch_related('visitors').get(id=tree_id)
    except Tree.DoesNotExist:
        return redirect ('dashboard')
    user_id = request.session['user_id']
    already_visited = tree.visitors.filter(id=user_id).exists()
    is_owner = (tree.mapped_by.id == user_id)
    context = {
        'tree': tree,
        'user_name': request.session.get('user_name'),
        'already_visited': already_visited,
        'is_owner': is_owner,
    }
    return render(request, 'tree_app/tree_detail.html', context)

def edit_tree(request, tree_id):
    if not request.session.get('user_id'):
        return redirect('index')
    try:
        tree = Tree.objects.get(id=tree_id)
    except Tree.DoesNotExist:
        return redirect('dashboard')
    if tree.mapped_by.id != request.session['user_id']:
        return redirect('dashboard')
    return render(request,'tree_app/edit_tree.html',{
        'tree': tree,
        'user_name': request.session.get('user_name'),
    })


def update_tree(request, tree_id):
    if not request.session.get('user_id'):
        return redirect('index')
    if request.method != 'POST':
        return redirect('edit_tree',tree_id=tree_id)
    try:
        tree = Tree.objects.get(id=tree_id)
    except Tree.DoesNotExist: 
        return redirect('dashboard') 
    if tree. mapped_by.id != request.session['user_id']:
        return redirect('dashboard')
    errors = Tree.objects.create_validator(request.POST)
    if errors:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('edit_tree', tree_id=tree_id)
    tree.species = request.POST['species']
    tree.location = request.POST['location']
    tree.date_found = request.POST['date_found']
    tree.zip_code = request.POST['zip_code', '']
    tree.notes = request.POST['notes', '']
    tree.save()
    return redirect('dashboard')

def delete_tree(request, tree_id):
    if not request.session.get('user_id'):
        return redirect('index')
    try:
        tree = Tree.objects.get(id=tree_id)
    except Tree.DoesNotExist:
        return redirect('dashboard')
    if tree.mapped_by.id==request.session['user_id']:
        tree.delete()
        return redirect('dashboard')
    return redirect('dashboard')

def visit_tree(request, tree_id):
    if not request.session.get('user_id'):
        return redirect('index')
    try:
        tree = Tree.objects.get(id=tree_id)
        user = User.objects.get(id=request.session['user_id'])
        if not tree.visitors.filter(id=user.id).exists():
            tree.visitors.add(user)
    except (Tree.DoesNotExist, User.DoesNotExist):
        pass
    return redirect('tree_detail', tree_id=tree_id)

def trees_by_zip(request, zip_code):
    if not request.session.get('user_id'):
        return redirect('index')
    trees = Tree.objects.filter(zip_code=zip_code)
    context = {
        'trees': trees,
        'zip_code': zip_code,
        'user_name': request.session.get('user_name'),
    }
    return render(request, 'tree_app/trees_by_zip.html', context)
    
            
            
            
            
            