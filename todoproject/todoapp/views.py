from django.shortcuts import render,redirect
from .models import Task
from .forms import TodoForm
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from  django.views.generic.edit import UpdateView,DeleteView


class Tasklistview(ListView):
    model = Task
    template_name = 'homepage.html'
    context_object_name = 'task1'


class  TaskDetailview(DetailView) :
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class Taskupadateview(UpdateView):
    model = Task
    template_name = 'update_view.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cvbdetails',kwargs={'pk':self.object.id})

class TaskeDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')








# Create your views here.
def add_task(request):
    taskk = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()

    return render(request,'homepage.html',{'taskk':taskk})


def details(request):
    task=Task.objects.all()
    return render(request,'details.html',{'task':task})

def delete(request,id):
    task=Task.objects.get(id=id)
    if request.method=="POST":
        task.delete()
        return redirect('/')

    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')

    return render(request,'update.html',{'f':f,'task':task})