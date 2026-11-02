from rest_framework import serializers
from .models import Homework

class HomeworkSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    countdown_info = serializers.ReadOnlyField(source='countdown')
    class Meta: model = Homework; fields = '__all__'
