from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import AppealsForm
from .send_mail import send_feedback_email


def index(request: HttpRequest) -> HttpResponse:
    """Модуль, отвечающий за форму обращения на странице"""
    if request.method == 'POST':
        form = AppealsForm(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            patronymic = form.cleaned_data['patronymic']
            phone = form.cleaned_data['phone']
            text = form.cleaned_data['text']
            send_feedback_email.delay(
                last_name,
                first_name,
                patronymic,
                phone,
                text)
            return HttpResponseRedirect('/')
    else:
        form = AppealsForm()
    return render(request, 'index.html', {'form': form})
