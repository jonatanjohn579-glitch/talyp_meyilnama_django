from rest_framework import serializers
from .models import TaskCategory, Task, SubTask

class SubTaskSerializer(serializers.ModelSerializer):
    class Meta: model = SubTask; fields = '__all__'

class TaskCategorySerializer(serializers.ModelSerializer):
    class Meta: model = TaskCategory; fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    subject_name = serializers.CharField(source='related_subject.name', read_only=True)
    countdown_info = serializers.ReadOnlyField(source='countdown')
    class Meta: model = Task; fields = '__all__'
