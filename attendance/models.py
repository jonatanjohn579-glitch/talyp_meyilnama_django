from django.db import models
from django.contrib.auth.models import User
from schedule.models import Subject

class AttendanceRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    attended_hours = models.PositiveIntegerField(default=0)
    missed_unexcused_hours = models.PositiveIntegerField(default=0)
    missed_excused_hours = models.PositiveIntegerField(default=0)
    max_allowed_hours = models.PositiveIntegerField(default=36)

    @property
    def is_critical(self): return self.missed_unexcused_hours >= self.max_allowed_hours

    @property
    def is_warning(self): return self.missed_unexcused_hours >= 24

    @property
    def remaining_allowed(self): return max(0, self.max_allowed_hours - self.missed_unexcused_hours)
