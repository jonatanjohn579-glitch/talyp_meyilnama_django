from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import TaskCategory, Task, SubTask
from .serializers import TaskSerializer, TaskCategorySerializer, SubTaskSerializer

def tasks_index(request):
    category_slug = request.GET.get('category')
    status_filter = request.GET.get('status', 'pending')
    tasks = Task.objects.all()
    if category_slug: tasks = tasks.filter(category__slug=category_slug)
    if status_filter == 'pending': tasks = tasks.filter(is_completed=False)
    elif status_filter == 'completed': tasks = tasks.filter(is_completed=True)
    return render(request, 'tasks/index.html', {'tasks': tasks, 'categories': TaskCategory.objects.all(), 'current_status': status_filter, 'current_category': category_slug})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('is_completed', 'deadline_date', 'deadline_time')
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def toggle_complete(self, request, pk=None):
        t = self.get_object(); t.is_completed = not t.is_completed; t.save()
        return Response(TaskSerializer(t).data)

class TaskCategoryViewSet(viewsets.ModelViewSet):
    queryset = TaskCategory.objects.all(); serializer_class = TaskCategorySerializer

class SubTaskViewSet(viewsets.ModelViewSet):
    queryset = SubTask.objects.all(); serializer_class = SubTaskSerializer
