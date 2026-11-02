from django.shortcuts import render
from rest_framework import viewsets
from .models import AttendanceRecord
from .serializers import AttendanceRecordSerializer

def attendance_index(request):
    return render(request, 'attendance/index.html', {'records': AttendanceRecord.objects.all()})

class AttendanceRecordViewSet(viewsets.ModelViewSet):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
