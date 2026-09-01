from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, reverse
from todo.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def index(request):
    tasks = Task.objects.filter(user__isnull=True)
    context = {
    'tasks': tasks,
    'num_tasks_not_started': tasks.filter(status='n').count(),
        'num_tasks_completed': tasks.filter(status='c').count(),
        'num_tasks_in_progress': tasks.filter(status='p').count(),
        'num_tasks_active':  tasks.filter(status='n').count() + tasks.filter(status='p').count(),
    }
    return render(request, template_name='index.html', context=context)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('login')

class UserTaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "user_tasks.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tasks = self.get_queryset()

        context['num_tasks_not_started'] = tasks.filter(status='n').count()
        context['num_tasks_completed'] = tasks.filter(status='c').count()
        context['num_tasks_in_progress'] = tasks.filter(status='p').count()
        context['num_tasks_active'] = tasks.filter(status='n').count() + tasks.filter(status='p').count()

        return context

class UserTaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = ['name', 'content','tags', 'status']
    template_name = "user_task_form.html"
    success_url = reverse_lazy('user_tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

class UserTaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Task
    template_name = "user_task_delete.html"
    context_object_name = "task"
    success_url = reverse_lazy('user_tasks')


    def test_func(self):
        return self.get_object().user == self.request.user

class UserTaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Task
    fields = ['name', 'content', 'tags', 'status']
    template_name = "user_task_form.html"

    def get_success_url(self):
        return reverse('user_tasks')

    def test_func(self):
        return self.get_object().user == self.request.user