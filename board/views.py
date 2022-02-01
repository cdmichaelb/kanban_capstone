from django.shortcuts import render
from rest_framework import viewsets, serializers
from .models import *
# Create your views here.

class KanbanViewSet(viewsets.ModelViewSet):
    queryset = Kanban.objects.all()
    serializer_class = serializers.ModelSerializer

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = serializers.ModelSerializer
    
class ColumnsViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = serializers.ModelSerializer
    
class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = serializers.ModelSerializer
    
class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = serializers.ModelSerializer
    
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.ModelSerializer
    
def index(request):
    return render(request, 'board/index.html')

def kanban(request):
    return render(request, 'board/kanban.html')

def tasks(request):
    return render(request, 'board/tasks.html')

def columns(request):
    return render(request, 'board/columns.html')

def notes(request):
    return render(request, 'board/notes.html')

def tags(request):
    return render(request, 'board/tags.html')

def users(request):
    return render(request, 'board/users.html')

def customuser(request):
    return render(request, 'board/customuser.html')

def kanban_api(request):
    return render(request, 'board/kanban_api.html')

def tasks_api(request):
    return render(request, 'board/tasks_api.html')

def columns_api(request):
    return render(request, 'board/columns_api.html')

def notes_api(request):
    return render(request, 'board/notes_api.html')

def tags_api(request):
    return render(request, 'board/tags_api.html')

def customuser_api(request):
    return render(request, 'board/customuser_api.html')

def admin(request):
    return render(request, 'board/admin.html')
