from django.db import models
from django.contrib.auth.models import User
from schedule.models import Subject
from core.utils import calculate_days_remaining

class TaskCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    color = models.CharField(max_length=50, default="#4f46e5")
    def __str__(self): return self.name

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL, null=True, related_name='tasks')
    related_subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    deadline_date = models.DateField()
    deadline_time = models.TimeField(default="18:00")
    priority = models.CharField(max_length=20, default='orta')
    is_completed = models.BooleanField(default=False)
    notes = models.TextField(blank=True, verbose_name="Bellikler")

    @property
    def countdown(self): return calculate_days_remaining(self.deadline_date, self.deadline_time)

    def __str__(self): return self.title

class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
