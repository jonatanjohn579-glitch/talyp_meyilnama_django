import datetime
from django.utils import timezone

def get_academic_week_number(target_date=None):
    if target_date is None:
        target_date = timezone.localtime(timezone.now()).date()
    return target_date.isocalendar()[1]

def get_current_week_type(target_date=None):
    """Sanawjy = 1-nji (Täç), Maýdalawjy = 2-nji (Jübüt)"""
    week_num = get_academic_week_number(target_date)
    return 'sanawjy' if week_num % 2 != 0 else 'maydalawjy'

def get_turkmen_day_name(target_date=None):
    if target_date is None:
        target_date = timezone.localtime(timezone.now()).date()
    days = {0: 'Duşenbe', 1: 'Sişenbe', 2: 'Çarşenbe', 3: 'Penşenbe', 4: 'Anna', 5: 'Şenbe', 6: 'Ýekşenbe'}
    return days.get(target_date.weekday(), 'Duşenbe')

def calculate_days_remaining(deadline_date, deadline_time=None):
    if not deadline_date:
        return {'status': 'unknown', 'text': '', 'days_diff': 0}
    now = timezone.localtime(timezone.now())
    if deadline_time:
        deadline_dt = timezone.make_aware(datetime.datetime.combine(deadline_date, deadline_time))
    else:
        deadline_dt = timezone.make_aware(datetime.datetime.combine(deadline_date, datetime.time(23, 59)))
    diff = deadline_dt - now
    diff_days = diff.days
    diff_seconds = diff.total_seconds()
    if diff_seconds < 0:
        return {'status': 'overdue', 'text': f"{abs(diff_days)} gün gijä galynan", 'days_diff': diff_days}
    elif diff_seconds <= 86400:
        return {'status': 'today', 'text': "Şu gün möhleti gutarýar", 'days_diff': 0}
    return {'status': 'upcoming', 'text': f"{diff_days} gün galdy", 'days_diff': diff_days}
