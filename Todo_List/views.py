from django.shortcuts import render
from .models import Task
from .forms import Create_new_task
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView


def home_page(request):
    context = {}
    list_of_tasks = Task.objects.all()
    context['all_tasks'] = list_of_tasks
    return render(request, 'home.html', context)

def create_task(request):

    if request.method == 'POST':
        form = Create_new_task(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/my_task')
    else:
        form = Create_new_task()
    return render(request, 'add_new_task.html',{'form':form})

class  detail_view(DetailView):
    model = Task





