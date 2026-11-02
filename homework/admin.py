from django.contrib import admin
from .models import Homework

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'due_date', 'due_time', 'priority', 'is_completed')
    list_filter = ('is_completed', 'priority', 'subject', 'due_date')
    search_fields = ('title', 'description', 'subject__name')
    actions = ['mark_completed']

    @admin.action(description="Saýlanan öý işlerini ýerine ýetirildi diýip belle")
    def mark_completed(self, request, queryset):
        queryset.update(is_completed=True)
