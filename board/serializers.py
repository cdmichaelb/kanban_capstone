from rest_framework import serializers
from .models import *
from users.serializers import UserDetailSerializer
from users.models import CustomUser

class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ['id', 'name', 'kanban', 'created_at', 'updated_at', 'user']
        extra_kwargs = {
            'user': {'required': False},
            'kanban': {'read_only': True}
            }
class KanbanSerializer(serializers.ModelSerializer):

    columns = ColumnSerializer(many=True)
    class Meta:
        model = Kanban
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'user', 'columns']
        extra_kwargs = {
            'user': {'required': False},
            'columns': {
                'required': False, 
                'read_only': True
                }
            }