from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('edit/game/<int:game_id>/', views.edit_game_view, name='edit_game'),
    path('game/<int:game_id>/', views.game_info_view, name='game_info'),
    path('game/<int:game_id>/delete/', views.delete_game_view, name='delete_game'),
    path('game/<int:game_id>/fav/', views.add_to_fav_view, name='add_to_fav'),
    path('game/<int:game_id>/rate/', views.rate_game_view, name='rate_game'),
    path('profile/<int:player_id>/', views.profile_view, name='profile'),
]