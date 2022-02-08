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
    serializer = KanbanSerializer(data=request.data)
    
    if serializer.is_valid():
        
        serializer.save()
        
        return Response(serializer.data)
    #print(serializer.errors)
    return Response(serializer.errors)

@api_view(['GET'])
def kanban_detail(request, pk):
    kanban = get_object_or_404(Kanban, pk=pk)
    serializer = KanbanDetailSerializer(kanban)
    return Response(serializer.data)
                    
@api_view(['GET'])
def kanban(request):
    kanbans = Kanban.objects.all()
    serializer = KanbanSerializer(kanbans, many=True)
    return Response(serializer.data)