import datetime
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from schedule.models import Subject, Teacher, BellPeriod, Lesson, StudentNote, ExamRecord
from tasks.models import TaskCategory, Task, SubTask
from homework.models import Homework
from attendance.models import AttendanceRecord

class Command(BaseCommand):
    help = 'Uniwersitet nusga maglumatlaryny (sapaklar, jaňlar, öý işleri, işler, ulanyjy) maglumat binýadyna goşýar'

    def handle(self, *args, **options):
        self.stdout.write("Nusga maglumatlar goşulýar...")

        # 0. Demo Ulanyjy we Superuser döretmek
        if not User.objects.filter(username='talyp').exists():
            user = User.objects.create_user(
                username='talyp',
                password='talyp123',
                first_name='Merdan',
                last_name='Amanow',
                email='talyp@talyp.lan'
            )
            profile = user.profile
            profile.role = 'talyp'
            profile.academic_group = 'Topar 301 (IT)'
            profile.student_id_number = 'T-2023-104'
            profile.save()
            self.stdout.write(self.style.SUCCESS("Demo ulanyjy döredildi: talyp / talyp123"))

        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_superuser(
                username='admin',
                password='admin123',
                email='admin@talyp.lan',
                first_name='Baş',
                last_name='Administrator'
            )
            if hasattr(admin_user, 'profile'):
                admin_user.profile.role = 'admin'
                admin_user.profile.academic_group = 'Dolandyryş'
                admin_user.profile.save()
            self.stdout.write(self.style.SUCCESS("Superuser (Admin) döredildi: admin / admin123"))

        # 1. Jaňlar
        bells_data = [
            (1, '1-nji para', '08:30', '10:00', 15),
            (2, '2-nji para', '10:15', '11:45', 45),
            (3, '3-nji para', '12:30', '14:00', 15),
            (4, '4-nji para', '14:15', '15:45', 15),
            (5, '5-nji para', '16:00', '17:30', 10),
        ]
        bell_objs = {}
        for num, name, start, end, brk in bells_data:
            b, _ = BellPeriod.objects.get_or_create(
                period_number=num,
                defaults={
                    'name': name,
                    'start_time': datetime.datetime.strptime(start, '%H:%M').time(),
                    'end_time': datetime.datetime.strptime(end, '%H:%M').time(),
                    'break_duration_minutes': brk,
                }
            )
            bell_objs[num] = b

        # 2. Sapaklar
        subjects_data = [
            ('Ýokary Matematika', 'MATH101', '#4f46e5'),
            ('Maglumat Ulgamlary we Programmirleme', 'CS201', '#059669'),
            ('Maglumat Howpsuzlygy', 'SEC301', '#dc2626'),
            ('Daşary Ýurt Dili (Iňlis dili)', 'ENG102', '#2563eb'),
            ('Maglumatlar Binýady (SQL)', 'DB202', '#7c3aed'),
            ('Kompýuter Torlary we Ulgamlary', 'NET302', '#d97706'),
            ('Türkmenistanyň Taryhy', 'HIS101', '#0d9488'),
            ('Magtymguly Pyragynyň Edebi Mirasy', 'LIT101', '#e11d48'),
        ]
        subject_objs = {}
        for name, code, color in subjects_data:
            s, _ = Subject.objects.get_or_create(name=name, defaults={'code': code, 'color': color})
            subject_objs[name] = s

        # 3. Mugallymlar
        teachers_data = [
            ('Dos. K. Ýusubow', 'Dosent', 'Matematika kafedrasy'),
            ('Uly mug. B. Meredowa', 'Uly mugallym', 'Kompýuter ylymlary kafedrasy'),
            ('Prof. O. Annaberdiýew', 'Professor', 'Maglumat howpsuzlygy kafedrasy'),
            ('Uly mug. Ş. Amanowa', 'Uly mugallym', 'Diller bölümi'),
            ('Dos. A. Gurbanow', 'Dosent', 'Maglumat ulgamlary'),
        ]
        teacher_objs = {}
        for name, title, office in teachers_data:
            t, _ = Teacher.objects.get_or_create(full_name=name, defaults={'title': title, 'office': office})
            teacher_objs[name] = t

        # 4. Raspisaniýa
        lessons_data = [
            ('Ýokary Matematika', 'Dos. K. Ýusubow', 'Aud. 308 (Baş bina)', 'monday', 1, 'both', 'leksiya', 'Integrallaryň barlag işi bar, formulalary gaýtalamaly.'),
            ('Maglumat Ulgamlary we Programmirleme', 'Uly mug. B. Meredowa', 'IT Lab 405', 'monday', 2, 'both', 'laboratoriya', 'Django ORM we Viewset tejribe işi barlanýar.'),
            ('Maglumat Howpsuzlygy', 'Prof. O. Annaberdiýew', 'Aud. 210', 'monday', 3, 'sanawjy', 'leksiya', 'Kriptografiýa açarlary boýunça leksiýa konspekti.'),
            ('Daşary Ýurt Dili (Iňlis dili)', 'Uly mug. Ş. Amanowa', 'Diller merkezi 204', 'tuesday', 1, 'both', 'tejribe', 'Prezentasiýa taýýarlamaly (AI in Education).'),
            ('Maglumatlar Binýady (SQL)', 'Dos. A. Gurbanow', 'Aud. 314', 'tuesday', 2, 'both', 'leksiya', 'Normalizasiýa we indeksasiýa temasy.'),
            ('Kompýuter Torlary we Ulgamlary', 'Prof. O. Annaberdiýew', 'Aud. 210', 'wednesday', 1, 'both', 'leksiya', 'TCP/IP protokollary we IP salgylandyryş.'),
            ('Ýokary Matematika', 'Dos. K. Ýusubow', 'Aud. 308', 'wednesday', 2, 'both', 'tejribe', 'Differensial deňlemeleriň amaly çözüwleri.'),
        ]
        for sub_name, teach_name, room, day, p_num, w_type, l_type, notes in lessons_data:
            Lesson.objects.get_or_create(
                subject=subject_objs[sub_name],
                day_of_week=day,
                period=bell_objs[p_num],
                week_type=w_type,
                defaults={
                    'teacher': teacher_objs.get(teach_name),
                    'auditorium': room,
                    'lesson_type': l_type,
                    'notes': notes,
                }
            )

        # 5. Iş bölümleri & Işler
        cat_okuw, _ = TaskCategory.objects.get_or_create(slug='okuw', defaults={'name': 'Okuw & Sapaklar', 'color': '#4f46e5'})
        cat_oy, _ = TaskCategory.objects.get_or_create(slug='oy_ishi', defaults={'name': 'Öý işleri', 'color': '#059669'})
        cat_synag, _ = TaskCategory.objects.get_or_create(slug='synag', defaults={'name': 'Synag taýýarlygy', 'color': '#e11d48'})
        
        today = datetime.date.today()
        t1, _ = Task.objects.get_or_create(
            title='Ýokary Matematika aralyk gözegçiligine gaýtalamak',
            defaults={
                'category': cat_synag,
                'related_subject': subject_objs['Ýokary Matematika'],
                'deadline_date': today + datetime.timedelta(days=2),
                'deadline_time': datetime.time(20, 0),
                'priority': 'yokary',
                'notes': 'Formulalar tablisasyny we barlag soraglaryny gaýtalamaly.',
            }
        )
        SubTask.objects.get_or_create(task=t1, title='Matrisalar we kesgitleýjiler', defaults={'is_completed': True})
        SubTask.objects.get_or_create(task=t1, title='Integral hasaplamalary', defaults={'is_completed': False})

        # 6. Öý işi
        Homework.objects.get_or_create(
            subject=subject_objs['Ýokary Matematika'],
            title='Differensial deňlemeler meseleleri',
            defaults={
                'description': '142-nji sahypadaky 12, 14, 15-nji meseleleri depdere çözmeli.',
                'due_date': today + datetime.timedelta(days=1),
                'due_time': datetime.time(8, 30),
                'priority': 'yokary',
                'attachments_note': 'A4 formatda ýa-da ýörite barlag depderinde tabşyrmaly.',
            }
        )
        Homework.objects.get_or_create(
            subject=subject_objs['Maglumat Ulgamlary we Programmirleme'],
            title='Django REST API CRUD taýýarlamak',
            defaults={
                'description': 'Viewset we Serializer arkaly talyplaryň işlerini dolandyrýan API ýazmaly.',
                'due_date': today + datetime.timedelta(days=3),
                'due_time': datetime.time(10, 15),
                'priority': 'orta',
                'attachments_note': 'GitHub linkini ýa-da zip faýly mugallyma tabşyrmaly.',
            }
        )

        # 7. Gatnaşyk
        AttendanceRecord.objects.get_or_create(
            subject=subject_objs['Ýokary Matematika'],
            defaults={'attended_hours': 32, 'missed_unexcused_hours': 4, 'max_allowed_hours': 36}
        )
        AttendanceRecord.objects.get_or_create(
            subject=subject_objs['Maglumat Ulgamlary we Programmirleme'],
            defaults={'attended_hours': 28, 'missed_unexcused_hours': 2, 'max_allowed_hours': 36}
        )

        # 8. Talybyň bellikleri (Student Notes)
        StudentNote.objects.get_or_create(
            title="Matematika formulalary we aralyk barlag konspekti",
            defaults={
                'subject': subject_objs['Ýokary Matematika'],
                'content': "Integrallar we matrisalar boýunça 5-nji sahypadaky formulalary gaýtalamaly. Barlag işinde 3 mesele berler.",
                'is_pinned': True,
            }
        )
        StudentNote.objects.get_or_create(
            title="Django REST API gollanma belligi",
            defaults={
                'subject': subject_objs['Maglumat Ulgamlary we Programmirleme'],
                'content': "ViewSet we ModelSerializer ulanylanda permission_classes goşmagy ýatdan çykarmaly däl.",
                'is_pinned': False,
            }
        )

        # 9. Synaglar
        ExamRecord.objects.get_or_create(
            subject=subject_objs['Maglumat Ulgamlary we Programmirleme'],
            exam_type='aralyk',
            date=today + datetime.timedelta(days=14),
            defaults={
                'time': datetime.time(9, 0),
                'auditorium': 'Lab 405',
                'topics_to_review': 'Python OOP, Django ORM, REST API CRUD soraglary.',
            }
        )

        self.stdout.write(self.style.SUCCESS("Nusga maglumatlar, talybyň bellikleri we admin hasaby üstünlikli goşuldy!"))
