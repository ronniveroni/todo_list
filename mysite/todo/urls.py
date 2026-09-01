from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('usertasks/', views.UserTaskListView.as_view(), name='user_tasks'),
    path('usertasks/create/', views.UserTaskCreateView.as_view(), name='user_task_create'),

]
