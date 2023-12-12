from django.shortcuts import render,redirect
from django.contrib import messages
from myapp.models import *
from myapp.forms import *
# Create your views here.

def index(request):
    item_list = ToDo.objects.order_by('-date')
    if(request.method == 'POST'):
        form = ToDoForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('todo')
    form = ToDoForm()
    page = {'forms': form, 'list': item_list, 'title': 'TODO LIST'}
    return render(request, 'index.html', page)  

def remove(request, item_id):
    item = ToDo.objects.get(id = item_id)
    item.delete()
    messages.info(request, "Item Removed!")
    return redirect('todo')     