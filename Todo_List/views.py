from django.shortcuts import render
from .models import Task
from .forms import Create_new_task
from django.http import HttpResponseRedirect


def home_page(request):
    context = {}
    list_of_tasks = Task.objects.all()
    context['all_tasks'] = list_of_tasks
    return render(request, 'home.html', context)

def create_task(request):
    context = {}
    form = Create_new_task(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['forms'] = form
    return render(request, 'add_new_task.html', context)

def add_task(request):
    title = request.POST['title']
    description = request.POST['description']
    new_item = Task(title = title, description = description)
    new_item.save()
    return  HttpResponseRedirect('my_task/')
# Create your views here.
