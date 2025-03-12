from django.urls import path
from . import views

urlpatterns = [
    path('checking/', views.auto_check_telegram, name='auto_check_telegram'),
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('crash/', views.crash_game, name='crash'),
]