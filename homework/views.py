from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Homework
from .serializers import HomeworkSerializer
from schedule.models import Subject

def homework_index(request):
    sub_id = request.GET.get('subject')
    st = request.GET.get('status', 'pending')
    hw = Homework.objects.all()
    if sub_id: hw = hw.filter(subject_id=sub_id)
    if st == 'pending': hw = hw.filter(is_completed=False)
    elif st == 'completed': hw = hw.filter(is_completed=True)
    return render(request, 'homework/index.html', {'homeworks': hw, 'subjects': Subject.objects.all(), 'current_status': st, 'selected_subject': sub_id})

class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all().order_by('is_completed', 'due_date', 'due_time')
    serializer_class = HomeworkSerializer

    @action(detail=True, methods=['post'])
    def toggle_complete(self, request, pk=None):
        h = self.get_object(); h.is_completed = not h.is_completed; h.save()
        return Response(HomeworkSerializer(h).data)
