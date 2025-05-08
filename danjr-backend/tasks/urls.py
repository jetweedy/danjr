from django.urls import path
from .views import TaskList, TaskDetail

urlpatterns = [
    path('', TaskList.as_view()),
    path('<str:task_id>/', TaskDetail.as_view()),
]
