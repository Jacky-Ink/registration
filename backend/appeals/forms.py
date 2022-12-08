from django import forms
from .models import Appeals


class AppealsForm(forms.ModelForm):
    last_name = forms.CharField(
        min_length=2,
        max_length=150,
        widget=forms.TextInput(
            attrs={'placeholder': 'Фамилия'}
        )
    )
    first_name = forms.CharField(
        min_length=2,
        max_length=150,
        widget=forms.TextInput(
            attrs={'placeholder': 'Имя'}
        )
    )
    patronymic = forms.CharField(
        min_length=2,
        max_length=150,
        widget=forms.TextInput(
            attrs={'placeholder': 'Отчество'}
        )
    )
    phone = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Введите номер телефона в формате 89001234567'}
        )
    )
    text = forms.CharField(
        min_length=10,
        widget=forms.Textarea(
            attrs={'placeholder': 'Опишите вашу проблему'}
        )
    )

    class Meta:
        model = Appeals
        fields = '__all__'
