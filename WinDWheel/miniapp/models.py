from django.db import models

class TelegramUser(models.Model):
    user_id = models.BigIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    balance = models.BigIntegerField(default=0)

    def __str__(self):
        return str(self.user_id)