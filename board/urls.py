from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>', views.kanban_detail, name='kanban_detail'),
    path('create/', views.kanban_create, name='kanban_create'),
    path('kanban/', views.kanban, name='kanban'),
    path('column/', views.column_create, name='column_create'),
    
]
