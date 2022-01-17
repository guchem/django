from django.urls import path
from .views import TodoDelete, TodoList, add_todo

app_name='todo'
urlpatterns = [
    path('',TodoList.as_view(), name='list'),
    path('add/', add_todo, name='add'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='delete')
]
