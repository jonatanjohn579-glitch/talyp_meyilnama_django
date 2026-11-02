from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

urlpatterns = [
    path('favicon.ico', lambda request: HttpResponse(status=204)),
    path('admin/', admin.site.urls),
    
    # Web views
    path('accounts/', include('accounts.urls')),
    path('', include('schedule.urls')),
    path('tasks/', include('tasks.urls')),
    path('homework/', include('homework.urls')),
    path('attendance/', include('attendance.urls')),
    
    # REST API endpoints
    path('api/auth/', include('accounts.api_urls')),
    path('api/schedule/', include('schedule.api_urls')),
    path('api/tasks/', include('tasks.api_urls')),
    path('api/homework/', include('homework.api_urls')),
    path('api/attendance/', include('attendance.api_urls')),
    path('api/bot/', include('bot.api_urls')),
]

admin.site.site_header = "TalypMeýilnama — Admin Dolandyryş Paneli"
admin.site.site_title = "TalypMeýilnama Admin"
admin.site.index_title = "Maglumatlar Bazasyny Dolandyrmak (Ähli Tablisalar)"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
