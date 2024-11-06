
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password, **extra_fields):

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        # Создание объекта пользователя с дополнительными полями
        user = self.model(phone_number=phone_number, **extra_fields)

        # Устанавливаем пароль отдельно
        user.set_password(password)

        # Возвращаем пользователя
        return user
