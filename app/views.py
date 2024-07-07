from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404
from.serializers import *
from.models import*


@api_view (['GET'])
def index (request):
    person1 ={
        "name":"Beauty",
        "age":29,
        "is_maried":False,
    }
    person2 ={
        "name":"Rabbia",
        "age":"28",
        "address":"kuncharpur",
        "is_marier":False
    }
    person_list=(person1, person2)
    return Response(person_list)

@api_view(['GET'])
def Todo_list (request):
    todos =Todo.object.all()
    
    serializer = TodoListSerializer(todos,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def todo_detail(request=id):
    todo=get_list_or_404(todo, id=id)
    serializer=TodoDetailSerializer(todo)
    return Response(serializer.data)

