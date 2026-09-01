from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from todo.models import Task
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    context = {
    'tasks': Task.objects.all(),
    'num_tasks_not_started': Task.objects.filter(status='n').count(),
    }
    return render(request, template_name='index.html', context=context)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('login')