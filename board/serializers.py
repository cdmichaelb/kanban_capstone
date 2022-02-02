from rest_framework import serializers
from .models import *
from users.serializers import UserDetailSerializer

class KanbanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanban
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')
        
class KanbanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanban
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')
        
class KanbanListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanban
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')
        
class KanbanCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanban
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')
        
class KanbanUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanban
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')
        
class KanbanDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanban
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')