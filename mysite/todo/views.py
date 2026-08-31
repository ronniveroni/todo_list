from django.shortcuts import render
from todo.models import Task

# Create your views here.
def index(request):
    context = {
    'tasks': Task.objects.all(),
    'num_tasks_not_started': Task.objects.filter(status='n').count(),
    }
    return render(request, template_name='index.html', context=context)
