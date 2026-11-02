from .utils import get_current_week_type, get_academic_week_number, get_turkmen_day_name
from django.utils import timezone

def talyp_context(request):
    now = timezone.localtime(timezone.now())
    active_week = get_current_week_type(now.date())
    return {
        'CURRENT_WEEK_TYPE': active_week,
        'CURRENT_WEEK_NAME': '1-nji hepde (Sanawjy)' if active_week == 'sanawjy' else '2-nji hepde (Maýdalawjy)',
        'CURRENT_WEEK_NUMBER': get_academic_week_number(now.date()),
        'CURRENT_DAY_NAME': get_turkmen_day_name(now.date()),
        'CURRENT_TIME': now.strftime('%H:%M'),
        'CURRENT_DATE': now.strftime('%d.%m.%Y'),
    }
