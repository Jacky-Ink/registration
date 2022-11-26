from django.db import models


class Contact(models.Model):
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия'
    )
    patronymic = models.CharField(
        max_length=150,
        verbose_name='Отчество'
    )
    phone = models.CharField(
        max_length=11,
        verbose_name='Номер телефона',
        help_text='Введите номер телефона в формате 89001234567'
    )
    text = models.TextField(
        verbose_name='Обращение',
        help_text='Опишите вашу проблему'
    )

    def __str__(self):
        return self.name
