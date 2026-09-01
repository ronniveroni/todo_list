from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('usertasks/', views.UserTaskListView.as_view(), name='user_tasks'),
    path('usertasks/create/', views.UserTaskCreateView.as_view(), name='user_task_create'),
    path('usertasks/<int:pk>/delete/', views.UserTaskDeleteView.as_view(), name='user_task_delete'),
    path('usertasks/<int:pk>/update/', views.UserTaskUpdateView.as_view(), name='user_task_update'),

]
