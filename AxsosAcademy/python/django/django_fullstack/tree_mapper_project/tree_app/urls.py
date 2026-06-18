from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('trees/new', views.new_tree, name='new_tree'),
    path('trees/create', views.create_tree, name='create_tree'),
    path('trees/<int:tree_id>', views.tree_detail, name='tree_detail'),
    path('trees/edit/<int:tree_id>', views.edit_tree, name='edit_tree'),
    path('trees/update/<int:tree_id>', views.update_tree, name='update_tree'),
    path('trees/delete/<int:tree_id>', views.delete_tree, name='delete_tree'),
    path('trees/visit/<int:tree_id>', views.visit_tree, name='visit_tree'),
    path('trees/zip/<str:zip_code>', views.trees_by_zip, name='trees_by_zip'),
]
    