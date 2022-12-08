from django.contrib import admin
from .models import Appeals


@admin.register(Appeals)
class AppealsAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'patronymic',
        'phone',
        'text'
    )
