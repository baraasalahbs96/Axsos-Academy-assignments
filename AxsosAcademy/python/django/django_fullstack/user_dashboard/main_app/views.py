from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User, Message, Comment

# ─── Helper ───────────────────────────────────────────
def get_user(request):
    if 'user_id' not in request.session:
        return None
    return User.objects.get(id=request.session['user_id'])

def is_admin(request):
    u = get_user(request)
    return u and u.user_level == 9

# ─── Public Pages ─────────────────────────────────────
def index(request):
    if 'user_id' in request.session:
        return redirect('/dashboard/')
    return render(request, 'main_app/index.html')

def signin(request):
    if 'user_id' in request.session:
        return redirect('/dashboard/')
    return render(request, 'main_app/signin.html')

def login(request):
    if request.method != 'POST':
        return redirect('/signin/')
    errors = User.objects.login_validator(request.POST)
    if errors:
        for val in errors.values():
            messages.error(request, val)
        return redirect('/signin/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    return redirect('/dashboard/')

def register_page(request):
    if 'user_id' in request.session:
        return redirect('/dashboard/')
    return render(request, 'main_app/register.html')

def register(request):
    if request.method != 'POST':
        return redirect('/register/')
    errors = User.objects.register_validator(request.POST)
    if errors:
        for val in errors.values():
            messages.error(request, val)
        return redirect('/register/')
    pw_hash = bcrypt.hashpw(
        request.POST['password'].encode(), bcrypt.gensalt()
    ).decode()
    # أول يوزر يصير admin تلقائياً
    level = 9 if User.objects.count() == 0 else 1
    user = User.objects.create(
        email      = request.POST['email'],
        first_name = request.POST['first_name'],
        last_name  = request.POST['last_name'],
        password   = pw_hash,
        user_level = level,
    )
    request.session['user_id'] = user.id
    return redirect('/dashboard/')

def logout(request):
    request.session.flush()
    return redirect('/')

# ─── Dashboard ────────────────────────────────────────
def dashboard(request):
    user = get_user(request)
    if not user:
        return redirect('/')
    context = {
        'user': user,
        'all_users': User.objects.all().order_by('id'),
    }
    return render(request, 'main_app/dashboard.html', context)

# ─── Admin: Manage Users ──────────────────────────────
def new_user(request):
    if not is_admin(request):
        return redirect('/dashboard/')
    return render(request, 'main_app/new_user.html', {'user': get_user(request)})

def create_user(request):
    if not is_admin(request):
        return redirect('/dashboard/')
    if request.method != 'POST':
        return redirect('/users/new/')
    errors = User.objects.register_validator(request.POST)
    if errors:
        for val in errors.values():
            messages.error(request, val)
        return redirect('/users/new/')
    pw_hash = bcrypt.hashpw(
        request.POST['password'].encode(), bcrypt.gensalt()
    ).decode()
    User.objects.create(
        email      = request.POST['email'],
        first_name = request.POST['first_name'],
        last_name  = request.POST['last_name'],
        password   = pw_hash,
        user_level = 1,
    )
    return redirect('/dashboard/')

def remove_user(request, uid):
    if not is_admin(request):
        return redirect('/dashboard/')
    User.objects.get(id=uid).delete()
    return redirect('/dashboard/')

def edit_user(request, uid):
    if not is_admin(request):
        return redirect('/dashboard/')
    context = {
        'user': get_user(request),
        'edit_user': User.objects.get(id=uid),
    }
    return render(request, 'main_app/edit_user.html', context)

def update_user(request, uid):
    if not is_admin(request):
        return redirect('/dashboard/')
    if request.method != 'POST':
        return redirect(f'/users/edit/{uid}/')
    u = User.objects.get(id=uid)
    u.email      = request.POST['email']
    u.first_name = request.POST['first_name']
    u.last_name  = request.POST['last_name']
    u.user_level = int(request.POST['user_level'])
    u.save()
    return redirect('/dashboard/')

def update_pw_admin(request, uid):
    if not is_admin(request):
        return redirect('/dashboard/')
    if request.method != 'POST':
        return redirect(f'/users/edit/{uid}/')
    if request.POST['password'] != request.POST['confirm_pw']:
        messages.error(request, "Passwords do not match.")
        return redirect(f'/users/edit/{uid}/')
    u = User.objects.get(id=uid)
    u.password = bcrypt.hashpw(
        request.POST['password'].encode(), bcrypt.gensalt()
    ).decode()
    u.save()
    return redirect('/dashboard/')

# ─── User Show + Messages ─────────────────────────────
def show_user(request, uid):
    user = get_user(request)
    if not user:
        return redirect('/')
    context = {
        'user': user,
        'profile': User.objects.get(id=uid),
        'wall_messages': Message.objects.filter(
            receiver_id=uid
        ).order_by('created_at'),
    }
    return render(request, 'main_app/show_user.html', context)

def post_message(request, uid):
    user = get_user(request)
    if not user:
        return redirect('/')
    if request.method != 'POST':
        return redirect(f'/users/show/{uid}/')
    if len(request.POST['content'].strip()) == 0:
        messages.error(request, "Message cannot be empty.")
        return redirect(f'/users/show/{uid}/')
    Message.objects.create(
        content  = request.POST['content'],
        sender   = user,
        receiver = User.objects.get(id=uid),
    )
    return redirect(f'/users/show/{uid}/')

def post_comment(request, mid):
    user = get_user(request)
    if not user:
        return redirect('/')
    if request.method != 'POST':
        return redirect('/')
    msg = Message.objects.get(id=mid)
    if len(request.POST['content'].strip()) == 0:
        return redirect(f'/users/show/{msg.receiver.id}/')
    Comment.objects.create(
        content = request.POST['content'],
        user    = user,
        message = msg,
    )
    return redirect(f'/users/show/{msg.receiver.id}/')

# ─── Own Profile Edit ─────────────────────────────────
def edit_profile(request):
    user = get_user(request)
    if not user:
        return redirect('/')
    return render(request, 'main_app/edit_profile.html', {'user': user})

def update_profile(request):
    user = get_user(request)
    if not user:
        return redirect('/')
    if request.method != 'POST':
        return redirect('/users/edit/')
    user.email      = request.POST['email']
    user.first_name = request.POST['first_name']
    user.last_name  = request.POST['last_name']
    user.save()
    return redirect('/users/edit/')

def update_pw(request):
    user = get_user(request)
    if not user:
        return redirect('/')
    if request.method != 'POST':
        return redirect('/users/edit/')
    if request.POST['password'] != request.POST['confirm_pw']:
        messages.error(request, "Passwords do not match.")
        return redirect('/users/edit/')
    if len(request.POST['password']) < 8:
        messages.error(request, "Password must be at least 8 characters.")
        return redirect('/users/edit/')
    user.password = bcrypt.hashpw(
        request.POST['password'].encode(), bcrypt.gensalt()
    ).decode()
    user.save()
    return redirect('/users/edit/')

def update_desc(request):
    user = get_user(request)
    if not user:
        return redirect('/')
    if request.method != 'POST':
        return redirect('/users/edit/')
    user.description = request.POST['description']
    user.save()
    return redirect('/users/edit/')