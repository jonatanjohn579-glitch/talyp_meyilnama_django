from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Lesson, BellPeriod, StudentNote
from tasks.models import Task
from homework.models import Homework
from attendance.models import AttendanceRecord
from .serializers import LessonSerializer, BellPeriodSerializer
from core.utils import get_current_week_type, get_turkmen_day_name

def schedule_index(request):
    now = timezone.localtime(timezone.now())
    active_week = get_current_week_type(now.date())
    day_codes = {0: 'monday', 1: 'tuesday', 2: 'wednesday', 3: 'thursday', 4: 'friday', 5: 'saturday', 6: 'monday'}
    today_code = day_codes.get(now.weekday(), 'monday')
    
    day_filter = request.GET.get('day', today_code)
    week_filter = request.GET.get('week', active_week)
    search_q = request.GET.get('q', '').strip()
    
    lessons = Lesson.objects.all().select_related('subject', 'teacher', 'period')
    if search_q:
        from django.db.models import Q
        lessons = lessons.filter(
            Q(subject__name__icontains=search_q) |
            Q(teacher__full_name__icontains=search_q) |
            Q(auditorium__icontains=search_q) |
            Q(notes__icontains=search_q)
        )
    else:
        if day_filter != 'all':
            lessons = lessons.filter(day_of_week=day_filter)
        if week_filter != 'all':
            from django.db.models import Q
            lessons = lessons.filter(Q(week_type='both') | Q(week_type=week_filter))
            
    bells = BellPeriod.objects.all().order_by('period_number')
    tasks = Task.objects.filter(is_completed=False).order_by('deadline_date')
    homeworks = Homework.objects.filter(is_completed=False).order_by('due_date')
    attendance_records = AttendanceRecord.objects.all()
    student_notes = StudentNote.objects.all().order_by('-is_pinned')
    lesson_notes = Lesson.objects.exclude(notes='').exclude(notes__isnull=True)
    
    return render(request, 'schedule/index.html', {
        'lessons': lessons.order_by('period__period_number'),
        'bells': bells,
        'tasks': tasks,
        'tasks_count': tasks.count(),
        'homeworks': homeworks,
        'homeworks_count': homeworks.count(),
        'attendance_records': attendance_records,
        'student_notes': student_notes,
        'lesson_notes': lesson_notes,
        'selected_day': day_filter,
        'selected_week': week_filter,
        'search_query': search_q,
        'today_code': today_code,
        'active_week': active_week,
        'today_day_name': get_turkmen_day_name(now.date()),
    })

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all().order_by('day_of_week', 'period__period_number')
    serializer_class = LessonSerializer

    @action(detail=False, methods=['get'])
    def today(self, request):
        now = timezone.localtime(timezone.now())
        day_map = {0: 'monday', 1: 'tuesday', 2: 'wednesday', 3: 'thursday', 4: 'friday', 5: 'saturday', 6: 'monday'}
        today_code = day_map.get(now.weekday(), 'monday')
        current_week = get_current_week_type(now.date())
        from django.db.models import Q
        lessons = Lesson.objects.filter(day_of_week=today_code).filter(Q(week_type='both') | Q(week_type=current_week)).order_by('period__period_number')
        return Response({'day': today_code, 'week_type': current_week, 'lessons': LessonSerializer(lessons, many=True).data})

class BellPeriodViewSet(viewsets.ModelViewSet):
    queryset = BellPeriod.objects.all().order_by('period_number')
    serializer_class = BellPeriodSerializer
