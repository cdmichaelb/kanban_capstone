from email.policy import default
from rest_framework import serializers
from .models import *
from users.serializers import UserDetailSerializer
from users.models import CustomUser

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'name', 'description', 'column', 'created_at', 'updated_at', 'user']
        extra_kwargs = {
            'user': {'required': False},
            'column': {'read_only': False, 'required': False, 'allow_null': True}
            }

class ColumnSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True, default=[])
    class Meta:
        model = Column
        fields = ['id', 'name', 'kanban', 'created_at', 'updated_at', 'index', 'user', 'cards']
        extra_kwargs = {
            'kanban': {
                'required': True,
                'read_only': False,
                'allow_null': False
                }
            }

class KanbanSerializer(serializers.ModelSerializer):
    columns = ColumnSerializer(many=True, default=[], read_only=True)
    class Meta:
        model = Kanban
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'user', 'columns']
        extra_kwargs = {
            'user': {'required': False},
            'columns': {
                'required': False, 
                'read_only': False,
                'allow_null': True
                }
            }


