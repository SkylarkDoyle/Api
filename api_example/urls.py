from django.urls import path
from .views import apiOverview, taskDelete, taskList, taskDetail, taskCreate, taskUpdate

urlpatterns = [
    path('', apiOverview, name='api-view'),
    path('task-list/', taskList, name='task-list'),
    path('task-detail/<int:id>', taskDetail, name='task-detail'),
    path('task-create/', taskCreate, name='task-create'),
    path('task-update/<int:id>', taskUpdate, name='task-update'),
    path('task-delete/<int:id>/', taskDelete, name='task-delete'),
]