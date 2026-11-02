from django.utils import timezone
from schedule.models import Lesson, BellPeriod
from tasks.models import Task
from homework.models import Homework
from core.utils import get_current_week_type

def handle_student_query(query_text):
    q = query_text.lower().strip()
    active_week = get_current_week_type()

    # Bellikler barada sorag
    if any(k in q for k in ['bellik', 'bellikler', 'ýazgy', 'konspekt', 'note']):
        lessons = Lesson.objects.exclude(notes='').exclude(notes__isnull=True)
        tasks = Task.objects.exclude(notes='').exclude(notes__isnull=True)
        items = []
        for l in lessons: items.append(f"• 📖 {l.subject.name}: {l.notes}")
        for t in tasks: items.append(f"• 📋 {t.title}: {t.notes}")
        if items: return "📝 *Ýatda saklanan bellikleriňiz:*" + "\n".join(items)
        return "📝 Häzirlikçe ýatda saklanan bellik ýok."

    if any(k in q for k in ['hepde', 'sanawjy', 'maydalawjy']):
        name = '1-nji hepde (Sanawjy)' if active_week == 'sanawjy' else '2-nji hepde (Maýdalawjy)'
        return f"📅 Häzirki işjeň hepde: *{name}*."

    if any(k in q for k in ['jan', 'jaň', 'para']):
        bells = BellPeriod.objects.all().order_by('period_number')
        lines = [f"• {b.name}: {b.start_time.strftime('%H:%M')} - {b.end_time.strftime('%H:%M')}" for b in bells]
        return "🔔 *Jaňlaryň wagtlary:*" + "\n".join(lines)

    return "🤖 Salam! Men TalypMeýilnama kömekçisi. Sorap bilersiňiz: Ýazan belliklerim, Şu günki sapaklar, jaň wagtlary, hepde görnüşi."
