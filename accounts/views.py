from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated: return redirect('schedule_index')
    if request.method == 'POST':
        u = request.POST.get('username', '').strip()
        p = request.POST.get('password', '').strip()
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            return redirect('schedule_index')
        messages.error(request, "Ulanyjy ady ýa-da parol nädogry.")
    return render(request, 'accounts/login.html')

def register_view(request):
    if request.user.is_authenticated: return redirect('schedule_index')
    if request.method == 'POST':
        fn = request.POST.get('full_name', '').strip()
        un = request.POST.get('username', '').strip().lower()
        pw = request.POST.get('password', '').strip()
        if len(pw) < 4:
            messages.error(request, "Parol azyndan 4 simwol bolmaly.")
            return render(request, 'accounts/register.html')
        user = User.objects.create_user(username=un, password=pw, first_name=fn)
        login(request, user)
        return redirect('schedule_index')
    return render(request, 'accounts/register.html')

def logout_view(request):
    logout(request)
    return redirect('login')
