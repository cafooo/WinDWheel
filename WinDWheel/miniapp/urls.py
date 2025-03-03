from django.urls import path
from .views import index, crash_game, profile

urlpatterns = [
    path('', index, name='index'),
    path('profile/', profile, name='profile'),
    path('crash/', crash_game, name='crash'),
]