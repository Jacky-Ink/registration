from celery.decorators import shared_task
from celery.utils.log import get_task_logger
from .send_mail import send_feedback_email

logger = get_task_logger(__name__)


@shared_task(name="send_feedback_email_task")
def send_feedback_email_task(
                             last_name,
                             first_name,
                             patronymic,
                             phone,
                             text):
    logger.info("Sent email")
    return send_feedback_email(
        last_name,
        first_name,
        patronymic,
        phone,
        text
        )
