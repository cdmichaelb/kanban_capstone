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
    path('column/<int:pk>', views.column_detail, name='column_detail'),
    path('card/', views.card_create, name='card_create'),
    path('card/<int:pk>', views.card_detail, name='card_detail'),
    path('card/delete/<int:pk>', views.card_delete, name='card_delete'),
    path('column/delete/<int:pk>', views.column_delete, name='column_delete'),
    path('kanban/delete/<int:pk>', views.kanban_delete, name='kanban_delete'),
    path('kanban/edit/<int:pk>', views.kanban_update, name='kanban_update'),
    path('column/edit/<int:pk>', views.column_update, name='column_update'),
    path('card/edit/<int:pk>', views.card_update, name='card_update'),
    #path('kanban/move/<int:pk>', views.kanban_move, name='kanban_move'),
    path('column/move/<int:pk>', views.column_index, name='column_index'),
    path('card/move/<int:pk>', views.card_move, name='card_move'),
]
