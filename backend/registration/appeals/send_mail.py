from django.core.mail import send_mail


def send_feedback_email(last_name, first_name, patronymic, phone, text):
    send_mail(
        last_name,
        first_name,
        patronymic,
        phone,
        text+" \n "+['recepients email'],
        fail_silently=False
        )
