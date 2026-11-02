from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('role', models.CharField(default='talyp', max_length=20)),
                ('academic_group', models.CharField(default='Topar 301 (IT)', max_length=100)),
                ('student_id_number', models.CharField(blank=True, max_length=50, null=True)),
                ('avatar_color', models.CharField(default='bg-indigo-600', max_length=30)),
                ('theme_preference', models.CharField(default='light', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
