from urllib import response
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
            'user': user.id,
            }
    
    serializer = KanbanSerializer(data=response.data, many=False)
    print(response.data)
    if serializer.is_valid():
        serializer.save()
        response.status_code = 201
        response.data = {
            'kanbans': serializer.data,
            'kanban_list': KanbanSerializer(Kanban.objects.filter(user=request.user), many=True).data
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
            'index': Column.objects.filter(kanban=newColumn.kanban).count(),
            'user': user.id
            }
    serializer = ColumnSerializer(data=response.data, many=False)
    if serializer.is_valid():
        serializer.save()
        response.status_code = 201
        response.data = {
            'columns': serializer.data,
            'column_list': ColumnSerializer(Column.objects.filter(kanban=newColumn.kanban), many=True).data            }
        print(response.data, " is valid")
    else:
        print(serializer.errors)
        response.status_code = 400
        response.data = {'message': 'Column could not be created'}
        print(response.data, " is not valid")
    
    return response

@api_view(['POST'])
def card_create(request):
    response = Response()
    newCard = Card(name=request.data['name'], description=request.data['description'], column=Column.objects.get(id=request.data['column']), user=request.user)
    
    user = CustomUser.objects.get(id=request.user.id)
    response.data = {
            'id': newCard.id,
            'name': newCard.name,
            'description': newCard.description,
            'column': newCard.column.id,
            'created_at': newCard.created_at,
            'updated_at': newCard.updated_at,
            'user': user.id,
            'index': newCard.column.index
            }
    serializer = CardSerializer(data=response.data, many=False)

    if serializer.is_valid():
        serializer.save()
        response.status_code = 201
        response.data = {
            #'cards': serializer.data,
            'column': newCard.column.id,
            'column_list': ColumnSerializer(Column.objects.filter(kanban=newCard.column.kanban), many=True).data,
            'card_list': CardSerializer(Card.objects.filter(column=newCard.column), many=True).data
            }
        print(response.data, " is valid")
    else:
        print(serializer.errors)
        response.status_code = 400
        response.data = {'message': 'Card could not be created'}
        print(response.data, " is not valid")
    
    return response

@api_view(['GET'])
def kanban(request):
    response = Response()
    kanbans = Kanban.objects.filter(user=request.user)
    cards = Card.objects.all()
    columns = Column.objects.all()
    serializer = KanbanSerializer(kanbans, many=True)
    serializer2 = CardSerializer(cards, many=True)
    serializer3 = ColumnSerializer(columns, many=True)
    response.data = {
        'kanbans_list': serializer.data,
        'card_list': serializer2.data,
        'columns': serializer3.data
        }
    return response

@api_view(['GET'])
def column_detail(request, pk):
    response = Response()
    column = Column.objects.filter(kanban=pk)
    serializer = ColumnSerializer(column, many=True)
    response.data = {'column_list': serializer.data}
    return response

@api_view(['GET'])
def kanban_detail(request, pk):
    kanban = get_object_or_404(Kanban, pk=pk)
    serializer = KanbanSerializer(kanban)
    return Response(serializer.data)

@api_view(['GET'])
def card_detail(request, pk):
    response = Response()
    card = Card.objects.filter(column=pk)
    serializer = CardSerializer(card, many=True)
    response.data = {'card_list': serializer.data}
    print(response.data)
    return Response(serializer.data)

@api_view(['DELETE'])
def card_delete(request, pk):
    card = get_object_or_404(Card, pk=pk)
    card.delete()
    response.data = {'message': 'Card deleted',
                    'card_list': CardSerializer(Card.objects.filter(column=card.column), many=True).data,
                    'column_list': ColumnSerializer(Column.objects.filter(kanban=card.column.kanban), many=True).data,
                    }
    
    return Response(response.data)

@api_view(['DELETE'])
def column_delete(request, pk):
    column = get_object_or_404(Column, pk=pk)
    column.delete()
    response.data = {'message': 'Column deleted',
                    'column_list': ColumnSerializer(Column.objects.filter(kanban=column.kanban), many=True).data,
                    }
    
    return Response(response.data)

@api_view(['DELETE'])
def kanban_delete(request, pk):
    print("Kanban delete ", pk)
    kanban = get_object_or_404(Kanban, pk=pk)
    kanban.delete()
    response.data = {'message': 'Kanban deleted',
                    'kanban_list': KanbanSerializer(Kanban.objects.filter(user=request.user), many=True).data,
                    'column_list': ColumnSerializer(Column.objects.filter(kanban=kanban), many=True).data,
                    'card_list': CardSerializer(Card.objects.filter(column__in=Column.objects.filter(kanban=kanban)), many=True).data,
                    
                    }
    
    return Response(response.data)

@api_view(['PUT'])
def card_update(request, pk):
    card = get_object_or_404(Card, pk=pk)
    serializer = CardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response.status_code = 201
        response.data = {
            'card': serializer.data,
            'card_list': CardSerializer(Card.objects.filter(column=card.column), many=True).data,
            'column_list': ColumnSerializer(Column.objects.filter(kanban=card.column.kanban), many=True).data,
            }
        print(response.data, " is valid")
    else:
        print(serializer.errors)
        response.status_code = 400
        response.data = {'message': 'Card could not be updated'}
        print(response.data, " is not valid")
    
    return Response(response.data)

@api_view(['PUT'])
def column_update(request, pk):
    column = get_object_or_404(Column, pk=pk)
    serializer = ColumnSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response.status_code = 201
        response.data = {
            'column': serializer.data,
            'column_list': ColumnSerializer(Column.objects.filter(kanban=column.kanban), many=True).data,
            }
        print(response.data, " is valid")
    else:
        print(serializer.errors)
        response.status_code = 400
        response.data = {'message': 'Column could not be updated'}
        print(response.data, " is not valid")
    
    return Response(response.data)

@api_view(['PUT'])
def kanban_update(request, pk):
    kanban = get_object_or_404(Kanban, pk=pk)
    serializer = KanbanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response.status_code = 201
        response.data = {
            'kanban': serializer.data,
            'kanban_list': KanbanSerializer(Kanban.objects.filter(user=request.user), many=True).data,
            }
        print(response.data, " is valid")
    else:
        print(serializer.errors)
        response.status_code = 400
        response.data = {'message': 'Kanban could not be updated'}
        print(response.data, " is not valid")
    
    return Response(response.data)

@api_view(['PUT'])
def column_move(request, pk):
    column = get_object_or_404(Column, pk=pk)
    
    serializer = ColumnSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response.status_code = 201
        response.data = {
            'column': serializer.data,
            'column_list': ColumnSerializer(Column.objects.filter(kanban=column.kanban), many=True).data,
            }
        print(response.data, " is valid")
    else:
        print(serializer.errors)
        response.status_code = 400
        response.data = {'message': 'Column could not be updated'}
        print(response.data, " is not valid")
    
    return Response(response.data)

@api_view(['PUT'])
def card_move(request, pk):
    data = request.data
    qs = Card.objects.filter(pk=pk)
    print(data['direction'])
    if qs.exists():
        card = qs.first()
        column = Column.objects.filter(pk=card.column.id).first()
        columns = Column.objects.filter(kanban=column.kanban)
        print(columns)
        print("s column id ", card.column.id)
        print("s column index ", card.column.index)
        print("card index: ", card.index)
        if data['direction'] == 'increase':
            if card.index >= len(columns):
                response.status_code = 400
                response.data = {'message': 'Card could not be moved'}
                print("Card could not be moved")
                return Response(response.data)
            card.index += 1
        elif data['direction'] == 'decrease':
            if card.index <= 0:
                response.status_code = 400
                response.data = {'message': 'Card could not be moved'}
                print("Card could not be moved")
                return Response(response.data)
            card.index -= 1
        print("card index2: ", card.index)
        for colu in columns:
            print ("column index ", colu.index)
            print ("column id ", colu.id)
            print("---------------------------------")
            if card.index == colu.index:
                print("match column id ", column.id)
                print("match colu id ", colu.id)
                print("match colu index ", colu.index)
                print("match card index ", card.index)
                
                card.column = colu
        print(card.column.id)
        card.save()
        response.status_code = 201
        response.data = {
            'card': CardSerializer(card).data,
            'card_list': CardSerializer(Card.objects.filter(column=card.column), many=True).data,
            'column_list': ColumnSerializer(Column.objects.filter(kanban=card.column.kanban), many=True).data,
            'kanban_list': KanbanSerializer(Kanban.objects.filter(user=request.user), many=True).data,
            }
        
        """
                        this.kanbans = response.data.kanbans_list;
                        this.kanbans.columns = response.data.column_list;
                        this.kanbans.cards = response.data.card_list;
                        this.kanbans.columns.cards = response.data.card_list;
                        this.kanban_count = Object.values(response.data.kanbans_list).length;
        """
        #print(response.data, " is valid")
    else:
        response.status_code = 400
        response.data = {'message': 'Card could not be updated'}
        print(response.data, " is not valid")

    return Response(response.data)

    
"""     card = get_object_or_404(Card, pk=pk)
    card = CardSerializer(Card.objects.filter(id=pk), many=True).data
    print("card: ", card)
    column = ColumnSerializer(Column.objects.filter(id=request.data['column_id']), many=True).data
    print("column: ", column)
    newIndex = int(column[0]['index']) + 1
    print("newIndex: ", newIndex)
    print("column[0]['kanban']", column[0]['kanban'])
    print(ColumnSerializer(Column.objects.filter(kanban=column[0]['kanban'])))
    newColumn = ColumnSerializer(Column.objects.filter(kanban=column[0]['kanban']), many=True).data
    
    print("new column: ", newColumn)
    print("newColumn 0: ", newColumn[0]['index'])
    print("newColumn 1: ", newColumn[1]['index'])
    print("newColumn 2: ", newColumn[2]['index'])
    # Print column of card """
    
"""     serializer = CardSerializer(data=response.data)
    
    if serializer.is_valid():
        serializer.save()
        response.status_code = 201
        response.data = {
            'card': serializer.data,
            'card_list': CardSerializer(Card.objects.filter(column=card.column), many=True).data,
            'column_list': ColumnSerializer(Column.objects.filter(kanban=card.column.kanban), many=True).data,
            }
        print(response.data, " is valid")
    else:
        print(serializer.errors)
        response.status_code = 400
        response.data = {'message': 'Card could not be updated'}
        print(response.data, " is not valid")
    
    return Response(response.data) """
