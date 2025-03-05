from django.shortcuts import render

def index(request):
    return render(request, 'miniapp/index.html')

def crash_game(request):
    return render(request, 'miniapp/crash.html')

def profile(request):
    return render(request, 'miniapp/profile.html')

