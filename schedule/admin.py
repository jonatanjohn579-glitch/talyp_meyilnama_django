from django.contrib import admin
from .models import Subject, Teacher, BellPeriod, Lesson, StudentNote, ExamRecord

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'color')
    search_fields = ('name', 'code')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'office')
    search_fields = ('full_name', 'title')

@admin.register(BellPeriod)
class BellPeriodAdmin(admin.ModelAdmin):
    list_display = ('period_number', 'name', 'start_time', 'end_time', 'break_duration_minutes')
    ordering = ('period_number',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('subject', 'day_of_week', 'period', 'lesson_type', 'week_type', 'auditorium', 'teacher')
    list_filter = ('day_of_week', 'week_type', 'lesson_type', 'subject')
    search_fields = ('subject__name', 'teacher__full_name', 'auditorium', 'notes')

@admin.register(StudentNote)
class StudentNoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'is_pinned', 'created_at')
    list_filter = ('is_pinned', 'subject')
    search_fields = ('title', 'content')

@admin.register(ExamRecord)
class ExamRecordAdmin(admin.ModelAdmin):
    list_display = ('subject', 'exam_type', 'date', 'time', 'auditorium')
    list_filter = ('exam_type', 'date', 'subject')
