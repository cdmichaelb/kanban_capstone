from rest_framework import serializers
from .models import *
from users.serializers import UserDetailSerializer
from users.models import CustomUser

class KanbanSerializer(serializers.ModelSerializer):
    #user = UserDetailSerializer()
    #print(user, " is user")
    class Meta:
        model = Kanban
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'user']
        extra_kwargs = {'user': {'required': False}}
        
class ColumnSerializer(serializers.ModelSerializer):
    #kanban = KanbanSerializer()
    #print(kanban, " is kanban")
    class Meta:
        model = Column
        fields = ['id', 'name', 'kanban', 'created_at', 'updated_at', 'user']
        extra_kwargs = {'user': {'required': False}}