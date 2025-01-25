from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    SEX = (
        ('male', 'Мужской'),
        ('female', 'Женский'),
    )

    class Roles(models.TextChoices):
        BOSS = 'boss', 'Руководитель'
        RECEPTION = 'reception', 'Рецепшн'
        EXECUTOR = 'executor', 'Исполнитель'
        CUSTOMER = 'customer', 'Клиент'

    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.CUSTOMER)
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='Номер телефона')
    sex = models.CharField(max_length=10, choices=SEX, verbose_name='Пол ', default='male')
    birthday = models.DateField(null=True, blank=True, verbose_name='Дата рождения ')
    date_of_registration = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.username
