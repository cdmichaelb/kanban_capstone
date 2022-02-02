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
    path('detail/', views.kanban_detail, name='kanban_detail'),
    path('create/', views.kanban_create, name='kanban_create'),
    #path('admin/', admin.site.urls),
    #path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='board/logout.html'), name='logout'),
    #path('users/', include('users.urls')),
    #path('signup/', views.signup, name='signup'),
    #path('boards/', include('boards.urls', namespace='boards')),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/profile/', views.profile, name='profile'),
    #path('accounts/profile/edit/', views.edit_profile, name='edit_profile'),
]
