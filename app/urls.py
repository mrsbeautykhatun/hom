
from django.urls import path
from.views import*

urlpatterns = [
    path('',index,name='index'),
    
    path('Todo_list/',Todo_list,name='Todo_list'),
   
    path('Todos/<int:id>/',todo_detail,name='todo_detail')

]