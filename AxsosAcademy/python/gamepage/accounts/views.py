from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Game, Rating, Favorite
from .forms import RegisterForm, GameForm


def login_view(request):
    register_form = RegisterForm()
    login_error = None
    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')
        if not email or not password:
            login_error = 'All fields are required'
        else:
            try:
                user_obj = CustomUser.objects.get(email=email)
                username = user_obj.username
            except CustomUser.DoesNotExist:
                username = email
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            login_error = 'Invalid email or password'

    return render(request, 'auth.html', {
        'register_form': register_form,
        'login_error': login_error,
    })


def register_view(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        register_form = RegisterForm()
    return render(request, 'auth.html', {'register_form': register_form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard_view(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.created_by = request.user
            game.save()
            return redirect('dashboard')
    else:
        form = GameForm()

    sort = request.GET.get('sort', 'name')
    direction = request.GET.get('dir', 'asc')
    allowed = {'name': 'name', 'genre': 'genre', 'release_date': 'release_date'}
    order_field = allowed.get(sort, 'name')
    if direction == 'desc':
        order_field = '-' + order_field
    games = Game.objects.all().order_by(order_field)
    next_dir = 'desc' if direction == 'asc' else 'asc'

    return render(request, 'dashboard.html', {
        'form': form, 'games': games, 'sort': sort, 'dir': direction, 'next_dir': next_dir,
    })


@login_required
def edit_game_view(request, game_id):
    game = get_object_or_404(Game, pk=game_id, created_by=request.user)
    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect('game_info', game_id=game.pk)
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_info', game_id=game.pk)
    else:
        form = GameForm(instance=game)
    return render(request, 'edit_game.html', {'form': form, 'game': game})


@login_required
def delete_game_view(request, game_id):
    game = get_object_or_404(Game, pk=game_id, created_by=request.user)
    if request.method == 'POST':
        game.delete()
    return redirect('dashboard')


@login_required
def add_to_fav_view(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'POST':
        Favorite.objects.get_or_create(user=request.user, game=game)
    return redirect('game_info', game_id=game.pk)


@login_required
def rate_game_view(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'POST':
        rate_value = request.POST.get('rate_value')
        if rate_value:
            Rating.objects.update_or_create(
                user=request.user, game=game, defaults={'rate': rate_value}
            )
    return redirect('game_info', game_id=game.pk)


@login_required
def game_info_view(request, game_id):
    game = get_object_or_404(Game, pk=game_id)

    sort = request.GET.get('sort', 'id')
    direction = request.GET.get('dir', 'asc')
    allowed = {'id': 'user__id', 'name': 'user__first_name', 'rate': 'rate'}
    order_field = allowed.get(sort, 'user__id')
    if direction == 'desc':
        order_field = '-' + order_field
    ratings = Rating.objects.filter(game=game).select_related('user').order_by(order_field)
    next_dir = 'desc' if direction == 'asc' else 'asc'

    return render(request, 'game_info.html', {
        'game': game,
        'ratings': ratings,
        'is_owner': game.created_by_id == request.user.id,
        'is_fav': Favorite.objects.filter(user=request.user, game=game).exists(),
        'my_rating': Rating.objects.filter(user=request.user, game=game).first(),
        'sort': sort, 'dir': direction, 'next_dir': next_dir,
    })


@login_required
def profile_view(request, player_id):
    profile_user = get_object_or_404(CustomUser, pk=player_id)
    favorites = Favorite.objects.filter(user=profile_user).select_related('game')
    return render(request, 'profile.html', {
        'profile_user': profile_user, 'favorites': favorites,
    })