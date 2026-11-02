from rest_framework.views import APIView
from rest_framework.response import Response
from .services import handle_student_query

class BotQueryAPIView(APIView):
    def post(self, request):
        q = request.data.get('query', '')
        return Response({'query': q, 'response': handle_student_query(q)})
