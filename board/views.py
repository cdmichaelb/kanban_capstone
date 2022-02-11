from urllib import response
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, serializers
from .models import *
from .serializers import *
# Create your views here.


def index(request):
    return render(request, 'board/index.html')

@api_view(['POST'])
def kanban_create(request):
    response = Response()

    newKanban = Kanban(name=request.data['name'], description=request.data['description'], user=request.user)
    
    user = CustomUser.objects.get(id=request.user.id)
    response.data = {
            'id': newKanban.id,
            'name': newKanban.name,
            'description': newKanban.description,
            'created_at': newKanban.created_at,
            'updated_at': newKanban.updated_at,
            'user': user.id
            }
    
    serializer = KanbanSerializer(data=response.data, many=False)

    if serializer.is_valid():
        serializer.save()
        response.status_code = 201
        response.data = {
            'kanbans': serializer.data,
            'kanban_list': KanbanSerializer(Kanban.objects.all(), many=True).data
            }  
        
    else:
        print(serializer.errors)
        response.status_code = 400
        response.data = {'message': 'Kanban could not be created'}
    
    return response

@api_view(['POST'])
def column_create(request):
    response = Response()

    newColumn = Column(name=request.data['name'], kanban=Kanban.objects.get(id=request.data['kanban']), user=request.user)
    
    user = CustomUser.objects.get(id=request.user.id)
    response.data = {
            'id': newColumn.id,
            'name': newColumn.name,
            'kanban': newColumn.kanban.id,
            'created_at': newColumn.created_at,
            'updated_at': newColumn.updated_at,
            'user': user.id
            }
    serializer = ColumnSerializer(data=response.data, many=False)

    if serializer.is_valid():
        serializer.save()
        response.status_code = 201
        response.data = {'columns': serializer.data}  
        print(response.data, " is valid")
    else:
        print(serializer.errors)
        response.status_code = 400
        response.data = {'message': 'Column could not be created'}
        print(response.data, " is not valid")
    
    return response

@api_view(['GET'])
def kanban(request):
    response = Response()
    kanbans = Kanban.objects.all()
    serializer = KanbanSerializer(kanbans, many=True)
    response.data = {'kanbans': serializer.data}
    return response

@api_view(['GET'])
def kanban_detail(request, pk):
    kanban = get_object_or_404(Kanban, pk=pk)
    serializer = KanbanSerializer(kanban)
    return Response(serializer.data)
                    





