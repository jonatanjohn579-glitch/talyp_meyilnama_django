from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='BellPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('period_number', models.PositiveSmallIntegerField(unique=True)),
                ('name', models.CharField(max_length=50)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('break_duration_minutes', models.PositiveSmallIntegerField(default=15)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(blank=True, max_length=20)),
                ('description', models.TextField(blank=True)),
                ('color', models.CharField(default='#4f46e5', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=200)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('office', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('auditorium', models.CharField(max_length=100)),
                ('day_of_week', models.CharField(max_length=20)),
                ('week_type', models.CharField(default='both', max_length=20)),
                ('lesson_type', models.CharField(default='leksiya', max_length=20)),
                ('notes', models.TextField(blank=True)),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.bellperiod')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='schedule.subject')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedule.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='StudentNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('is_pinned', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_notes', to='schedule.subject')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson_notes', to='schedule.lesson')),
            ],
        ),
    ]
