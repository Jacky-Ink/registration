# Generated by Django 3.2.16 on 2022-11-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeals', '0003_rename_contact_appeals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeals',
            name='phone',
            field=models.IntegerField(help_text='Введите номер телефона в формате 89001234567', verbose_name='Номер телефона'),
        ),
    ]
