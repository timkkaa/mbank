
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models





class CustomUser(AbstractUser):
    """Модель для кастомного пользователя"""

    phone_number = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(6)],
        unique=True,
    )
    balance = models.PositiveBigIntegerField(default=0)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Кастомный пользователь'
        verbose_name_plural = 'Кастомные пользователи'
