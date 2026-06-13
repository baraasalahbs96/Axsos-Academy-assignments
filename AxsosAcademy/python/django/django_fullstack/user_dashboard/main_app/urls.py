from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('login/', views.login, name='login'),
    path('register/', views.register_page, name='register_page'),
    path('register/submit/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Users (admin only)
    path('users/new/', views.new_user, name='new_user'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/remove/<int:uid>/', views.remove_user, name='remove_user'),
    path('users/edit/<int:uid>/', views.edit_user, name='edit_user'),
    path('users/update/<int:uid>/', views.update_user, name='update_user'),
    path('users/update_pw/<int:uid>/', views.update_pw_admin, name='update_pw_admin'),

    # User show page + messages
    path('users/show/<int:uid>/', views.show_user, name='show_user'),
    path('messages/post/<int:uid>/',  views.post_message,  name='post_message'),
    path('comments/post/<int:mid>/', views.post_comment,  name='post_comment'),

    # Profile (own)
    path('users/edit/', views.edit_profile, name='edit_profile'),
    path('users/update/', views.update_profile, name='update_profile'),
    path('users/update_pw/', views.update_pw, name='update_pw'),
    path('users/update_desc/',  views.update_desc, name='update_desc'),
]