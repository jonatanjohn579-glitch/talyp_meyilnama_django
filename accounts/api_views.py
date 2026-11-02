from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

@api_view(['POST'])
@permission_classes([AllowAny])
def api_login(request):
    u = request.data.get('username', '').strip()
    p = request.data.get('password', '').strip()
    user = authenticate(request, username=u, password=p)
    if user:
        login(request, user)
        return Response({'status': 'success', 'user': {'username': user.username}})
    return Response({'status': 'error', 'message': 'Ýalňyş maglumat'}, status=401)

@api_view(['POST'])
@permission_classes([AllowAny])
def api_register(request):
    u = request.data.get('username', '').strip().lower()
    p = request.data.get('password', '').strip()
    if User.objects.filter(username=u).exists():
        return Response({'status': 'error', 'message': 'Bu ulanyjy ady bar'}, status=400)
    user = User.objects.create_user(username=u, password=p)
    login(request, user)
    return Response({'status': 'success', 'user': {'username': user.username}}, status=201)

@api_view(['GET'])
def api_me(request):
    if not request.user.is_authenticated: return Response({'isAuthenticated': False})
    return Response({'isAuthenticated': True, 'username': request.user.username})
