from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import TaskForm
# Create your views here.
def index(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        tasks=Task.objects.all()
        form=TaskForm()
    return render(request,'tasks/list.html',{'tasks':tasks,'form':form})

def update(request,id):
    task=Task.objects.get(id=id)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form=TaskForm(instance=task)
    return render(request,'tasks/update_tasks.html',{'form':form})

def delete(request,id):
    item=Task.objects.get(id=id)
    if request.method=='POST':
        item.delete()
        return redirect('/')
    return render(request,'tasks/delete.html',{'item':item})
