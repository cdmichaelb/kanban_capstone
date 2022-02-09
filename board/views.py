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
    #kanbans = list(Kanban.objects.all().order_by('-created_at').values())
    #kanbans = list(Kanban.objects.filter(user=request.user).values())
    #serializer = KanbanSerializer(data=kanbans, many=True)

    newKanban = Kanban.objects.create(name=request.data['name'], description=request.data['description'], user=request.user)
    
    # Should probably use messages here
    if newKanban is not None:
        response.status_code = 201
        #response.data = {'kanbans': serializer.data}
    else:
        response.status_code = 400
        response.data = {'message': 'Kanban could not be created'}

    """     if serializer.is_valid():
        serializer.save()
        response.status_code = 201
        response.data = {'kanbans': serializer.data}  
        print(response.data, " is valid")
    else:
        print(serializer.errors)
        response.status_code = 400
        response.data = {'message': 'Kanban could not be created'}
        print(response.data, " is not valid") """

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