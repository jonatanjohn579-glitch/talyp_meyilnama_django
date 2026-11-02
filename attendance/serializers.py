from rest_framework import serializers
from .models import AttendanceRecord

class AttendanceRecordSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    is_critical = serializers.ReadOnlyField()
    is_warning = serializers.ReadOnlyField()
    remaining_allowed = serializers.ReadOnlyField()
    class Meta: model = AttendanceRecord; fields = '__all__'
