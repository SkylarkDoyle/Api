from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list',
        'Detail View': '/task-detail/<int:id>',
        'Create': '/task-create/',
        'Update': '/task-update/<int:id>',
        'Delete': 'task-delete/<int:id>/'
    }

    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True) 
    return Response(serializer.data)



@api_view(['GET'])
def taskDetail(request, id):
    tasks = Task.objects.get(id=id)
    serializer = TaskSerializer(tasks, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, id):
    tasks = Task.objects.get(id=id)
    serializer = TaskSerializer(instance=tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, id):
    tasks = Task.objects.get(id=id)
    tasks.delete()
    return Response('Successfully deleted')


