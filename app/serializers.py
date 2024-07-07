from rest_framework import serializers 
from.models import*



class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exelude=()

class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model =Todo
        field='__all__'
        depth =1

