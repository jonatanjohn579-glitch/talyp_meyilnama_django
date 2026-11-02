from django.contrib import admin
from .models import BotQueryLog

@admin.register(BotQueryLog)
class BotQueryLogAdmin(admin.ModelAdmin):
    list_display = ('query_text', 'user', 'created_at')
    search_fields = ('query_text', 'response_text')
    list_filter = ('created_at',)
