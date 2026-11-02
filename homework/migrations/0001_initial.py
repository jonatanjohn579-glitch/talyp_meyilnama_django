from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [('schedule', '0001_initial')]
    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('due_time', models.TimeField(default='08:30')),
                ('priority', models.CharField(default='orta', max_length=20)),
                ('is_completed', models.BooleanField(default=False)),
                ('attachments_note', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homeworks', to='schedule.subject')),
            ],
        ),
    ]
