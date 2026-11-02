from django.db import models
from django.contrib.auth.models import User

class BotQueryLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    query_text = models.CharField(max_length=500, verbose_name="Talybyň soragy")
    response_text = models.TextField(verbose_name="Botuň jogaby")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Bot sorag ýazgysy"
        verbose_name_plural = "AI Bot soraglary"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.query_text[:50]}... ({self.created_at.strftime('%d.%m.%Y')})"
