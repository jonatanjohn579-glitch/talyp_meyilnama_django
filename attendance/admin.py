from django.contrib import admin
from .models import AttendanceRecord

@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('subject', 'attended_hours', 'missed_unexcused_hours', 'missed_excused_hours', 'max_allowed_hours')
    list_filter = ('subject',)
    search_fields = ('subject__name',)
