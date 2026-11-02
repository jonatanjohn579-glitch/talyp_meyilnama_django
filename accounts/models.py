from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, default='talyp')
    academic_group = models.CharField(max_length=100, default='Topar 301 (IT)')
    student_id_number = models.CharField(max_length=50, blank=True, null=True)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created: UserProfile.objects.create(user=instance)
