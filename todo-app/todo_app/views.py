from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDoItem
from .forms import ToDoForm

# View all tasks and options to add, edit, delete
def todo_list(request):
    items = ToDoItem.objects.all()
    return render(request, 'todo_list.html', {'items': items})

# Add a new task
def add_todo_item(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = ToDoForm()
    return render(request, 'add_edit_todo_item.html', {'form': form, 'type': 'Add'})

# Edit an existing task
def edit_todo_item(request, id):
    item = get_object_or_404(ToDoItem, id=id)
    if request.method == "POST":
        form = ToDoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = ToDoForm(instance=item)
    return render(request, 'add_edit_todo_item.html', {'form': form, 'type': 'Edit'})

# Delete a task
def delete_todo_item(request, id):
    item = get_object_or_404(ToDoItem, id=id)
    if request.method == "POST":
        item.delete()
        return redirect('todo_list')
    return render(request, 'confirm_delete.html', {'item': item})