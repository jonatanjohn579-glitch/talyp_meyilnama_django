from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=200, verbose_name="Sapagyň ady")
    code = models.CharField(max_length=20, blank=True)
    color = models.CharField(max_length=50, default="#4f46e5")
    def __str__(self): return self.name

class Teacher(models.Model):
    full_name = models.CharField(max_length=200)
    title = models.CharField(max_length=100, blank=True)
    office = models.CharField(max_length=100, blank=True)
    def __str__(self): return self.full_name

class BellPeriod(models.Model):
    period_number = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    break_duration_minutes = models.PositiveSmallIntegerField(default=15)
    def __str__(self): return f"{self.name} ({self.start_time}-{self.end_time})"

class Lesson(models.Model):
    WEEK_CHOICES = [('both', 'Her hepde'), ('sanawjy', '1-nji hepde (Sanawjy)'), ('maydalawjy', '2-nji hepde (Maýdalawjy)')]
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='lessons')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    auditorium = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=20)
    period = models.ForeignKey(BellPeriod, on_delete=models.CASCADE)
    week_type = models.CharField(max_length=20, choices=WEEK_CHOICES, default='both')
    lesson_type = models.CharField(max_length=20, default='leksiya')
    notes = models.TextField(blank=True, verbose_name="Bellikler")
    def __str__(self): return f"{self.subject.name} ({self.day_of_week})"

class StudentNote(models.Model):
    title = models.CharField(max_length=255, verbose_name="Belligiň ady / Temasy")
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True, related_name='student_notes')
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, blank=True, related_name='lesson_notes')
    content = models.TextField(verbose_name="Bellik mazmuny (Ýazgy / Konspekt)")
    is_pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return self.title

class ExamRecord(models.Model):
    EXAM_CHOICES = [('aralyk', 'Aralyk gözegçilik'), ('jemleyji_synag', 'Jemleýji synag'), ('zacyot', 'Zaçýot')]
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='exams')
    exam_type = models.CharField(max_length=30, choices=EXAM_CHOICES, default='jemleyji_synag')
    date = models.DateField()
    time = models.TimeField(default="09:00")
    auditorium = models.CharField(max_length=100)
    examiner = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    topics_to_review = models.TextField(blank=True)
    def __str__(self): return f"{self.get_exam_type_display()}: {self.subject.name}"
