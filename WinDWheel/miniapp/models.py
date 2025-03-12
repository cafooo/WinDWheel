from django.db import models
import random
from decimal import Decimal

class TelegramUser(models.Model):
    user_id = models.BigIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return str(self.user_id)

class Game(models.Model):
    crash_point = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_finished = models.BooleanField(default=False)

    @staticmethod
    def calculate_multiplier(elapsed_time):
        # Используем тот же коэффициент роста, что и на клиенте
        growth_factor = 0.06
        return pow(2.718281828, growth_factor * elapsed_time)

    @staticmethod
    def generate_crash_point():
        RTP = 0.96
        
        # Определяем диапазоны множителей и их вероятности
        ranges = [
            (1.01, 2.00, 0.60),    # 60% шанс множителя от 1.01x до 2.00x
            (2.01, 5.00, 0.25),    # 25% шанс множителя от 2.01x до 5.00x
            (5.01, 10.00, 0.10),   # 10% шанс множителя от 5.01x до 10.00x
            (10.01, 25.00, 0.04),  # 4% шанс множителя от 10.01x до 25.00x
            (25.01, 50.00, 0.01)   # 1% шанс множителя от 25.01x до 50.00x
        ]
        
        r = random.random()
        cumulative_prob = 0
        
        for min_mult, max_mult, prob in ranges:
            cumulative_prob += prob
            if r <= cumulative_prob:
                # Генерируем множитель в выбранном диапазоне
                crash_point = min_mult + (max_mult - min_mult) * random.random()
                # Применяем корректировку RTP
                crash_point = crash_point * RTP
                # Округляем до 2 знаков после запятой
                return round(crash_point * 100) / 100
        
        return 1.01

    def __str__(self):
        return f"Game {self.id} - Crash at {self.crash_point}x"

    class Meta:
        ordering = ['-created_at']

class Bet(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    cashout_multiplier = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    is_won = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    cashout_time = models.DateTimeField(null=True)

    class Meta:
        indexes = [
            models.Index(fields=['user', 'game']),
        ]