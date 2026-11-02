from django.db import models
from schedule.models import Subject
from core.utils import calculate_days_remaining

class Homework(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='homeworks')
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    due_time = models.TimeField(default="08:30")
    priority = models.CharField(max_length=20, default='orta')
    is_completed = models.BooleanField(default=False)
    attachments_note = models.CharField(max_length=255, blank=True)

    @property
    def countdown(self): return calculate_days_remaining(self.due_date, self.due_time)

    def __str__(self): return f"{self.subject.name}: {self.title}"
