from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [('schedule', '0001_initial')]
    operations = [
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('attended_hours', models.PositiveIntegerField(default=0)),
                ('missed_unexcused_hours', models.PositiveIntegerField(default=0)),
                ('missed_excused_hours', models.PositiveIntegerField(default=0)),
                ('max_allowed_hours', models.PositiveIntegerField(default=36)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='schedule.subject')),
            ],
        ),
    ]
