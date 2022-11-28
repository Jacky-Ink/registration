from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import AppealsForm


def index(request: HttpRequest) -> HttpResponse:
    """Модуль, отвечающий за форму обращения на странице"""
    context = {
    }
    if request.method == 'POST':
        form = AppealsForm(request.POST)
        if form.is_valid():
            send_message(
                form.cleaned_data['last_name'],
                form.cleaned_data['first_name'],
                form.cleaned_data['patronymic'],
                form.cleaned_data['phone'],
                form.cleaned_data['text']
            )
            context = {'success': 1}
            form.save()
    else:
        form = AppealsForm()
    context['form'] = form
    return render(request, 'index.html', context=context)


def send_message(last_name, first_name, patronymic, phone, text):
    pass
