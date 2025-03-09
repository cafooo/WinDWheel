from django.urls import path
from .views import index, crash_game, profile, auto_check_telegram

urlpatterns = [
    path('checking/', auto_check_telegram, name='auto_check_telegram'),
    path('', index, name='index'),
    path('profile/', profile, name='profile'),
    path('crash/', crash_game, name='crash'),
]