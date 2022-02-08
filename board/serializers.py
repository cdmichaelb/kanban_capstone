from rest_framework import serializers
from .models import *
from users.serializers import UserDetailSerializer

class KanbanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanban
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')
        