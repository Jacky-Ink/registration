from celery import Celery
from celery.schedules import crontab
from appeals.send_mail import send_feedback_email

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, send_feedback_email.s('Yourname',
                                                         'yourlogin@xyz.com',
                                                         'Hello'), name='add every 10')


@app.task
def send_feedback_email_task(
        last_name,
        first_name,
        patronymic,
        phone,
        text):
    send_feedback_email(
        last_name,
        first_name,
        patronymic,
        phone,
        text)
    logger.info("Sent email")
