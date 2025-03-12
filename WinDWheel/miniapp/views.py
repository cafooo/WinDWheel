from django.shortcuts import render
from .models import TelegramUser



def index(request):
    user_id = request.GET.get('user_id')
    print(user_id)
    if user_id is not None:
        try:
            return render(request, template_name='miniapp/index.html', context={'user_id': user_id})
        except TelegramUser.DoesNotExist:
            return render(request, 'miniapp/error.html', {'message': f"User not found."})
    else:   
        return render(request, 'miniapp/error.html', 
                      {'message': "Some of required data is missing. Please provide screenshot of this error and send it to @your_moderation_id."})


def crash_game(request):
    user_id = request.GET.get('user_id')
    if user_id is not None:
        try:
            user = TelegramUser.objects.get(user_id=user_id)
            return render(request, template_name='miniapp/crash.html', context={
                'user_id': user_id,
                'balance': round(user.balance, 2)  # Округляем баланс при отображении
            })
        except TelegramUser.DoesNotExist:
            return render(request, 'miniapp/error.html', {'message': f"User not found."})
    else:
        return render(request, 'miniapp/error.html', 
                     {'message': "Some of required data is missing. Please provide screenshot of this error and send it to @your_moderation_id."})


def profile(request):
    user_id = request.GET.get('user_id')
    if user_id is not None:
        try:
            user = TelegramUser.objects.get(user_id=user_id)
            return render(request, template_name='miniapp/profile.html', context={'user_id': user_id,
                                                                                'balance': user.balance})
        except TelegramUser.DoesNotExist:
            return render(request, 'miniapp/error.html', {'message': f"User not found."})
    else:
        return render(request, 'miniapp/error.html', {'message': "Some of required data is missing. Please provide screenshot of this error and send it to @your_moderation_id."})

def check_telegram_user(user_id):
    try:
        user = TelegramUser.objects.get(user_id=user_id)
        return True, f"User {user_id} already exists."
    except TelegramUser.DoesNotExist:
        TelegramUser.objects.create(user_id=user_id)
        return False, f"User {user_id} created successfully."

def auto_check_telegram(request):
    user_id = request.GET.get('user_id')  # Получаем user_id из параметров запроса
    if user_id is not None:
        try:
            user_id = int(user_id)  # Преобразуем в целое число
            exists, message = check_telegram_user(user_id)
            
            if exists:
                return render(request, template_name='miniapp/index.html', context={'user_id': user_id})
            else:
                return render(request, template_name='miniapp/index.html', context={'user_id': user_id})
        except ValueError:
            message = "Invalid user_id. Please provide a valid integer."
            return render(request, 'miniapp/error.html', {'message': message})
    else:
        message = "Some of required data is missing. Please provide screenshot of this error and send it to @your_moderation_id."
        return render(request, 'miniapp/error.html', {'message': message})

