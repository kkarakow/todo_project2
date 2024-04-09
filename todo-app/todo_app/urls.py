from django.urls import path
from .views import todo_list, add_todo_item, edit_todo_item, delete_todo_item

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('add/', add_todo_item, name='add_todo_item'),
    path('edit/<int:id>/', edit_todo_item, name='edit_todo_item'),
    path('delete/<int:id>/', delete_todo_item, name='delete_todo_item'),
]