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

    newKanban = Kanban.objects.create(name=request.data['name'], description=request.data['description'], user=request.user)
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
        response.data = {'kanbans': serializer.data}  
        print(response.data, " is valid")
    else:
        print(serializer.errors)
        response.status_code = 400
        response.data = {'message': 'Kanban could not be created'}
        print(response.data, " is not valid")
    
    return response


@api_view(['GET'])
def kanban_detail(request, pk):
    kanban = get_object_or_404(Kanban, pk=pk)
    serializer = KanbanSerializer(kanban)
    return Response(serializer.data)
                    
@api_view(['GET'])
def kanban(request):
    kanbans = Kanban.objects.all()
    serializer = KanbanSerializer(kanbans, many=True)
    return Response(serializer.data)