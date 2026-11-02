from rest_framework import serializers
from .models import Subject, Teacher, BellPeriod, Lesson

class SubjectSerializer(serializers.ModelSerializer):
    class Meta: model = Subject; fields = '__all__'

class BellPeriodSerializer(serializers.ModelSerializer):
    class Meta: model = BellPeriod; fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    teacher_name = serializers.CharField(source='teacher.full_name', read_only=True)
    period_number = serializers.IntegerField(source='period.period_number', read_only=True)
    start_time = serializers.TimeField(source='period.start_time', read_only=True)
    end_time = serializers.TimeField(source='period.end_time', read_only=True)
    class Meta: model = Lesson; fields = '__all__'
