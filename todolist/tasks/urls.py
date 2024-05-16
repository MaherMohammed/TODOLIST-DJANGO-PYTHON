from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.registerView, name='register'),
    path('', views.homeView, name='home'),
    path('create-list/', views.createListView, name='create-list'),
    path('create-task/<str:pk>/', views.createTaskView, name='create-task'),
     path('update-task/<str:pk>/', views.updateTaskStatusView, name='update-task'),
]