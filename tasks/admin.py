from django.contrib import admin
from .models import TaskCategory, Task, SubTask

class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1

@admin.register(TaskCategory)
class TaskCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'related_subject', 'deadline_date', 'deadline_time', 'priority', 'is_completed')
    list_filter = ('is_completed', 'priority', 'category', 'deadline_date')
    search_fields = ('title', 'notes')
    inlines = [SubTaskInline]
    actions = ['mark_as_completed']

    @admin.action(description="Saýlanan işleri tamamlandy diýip belle")
    def mark_as_completed(self, request, queryset):
        queryset.update(is_completed=True)

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'is_completed')
    list_filter = ('is_completed',)
