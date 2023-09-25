from django.core.mail import send_mail
from django.conf import settings


class CustomerEmailService:
    @classmethod
    def send_email(cls, robot, recipient_list):
        subject = "Робот доступен"
        message = (
            f"Добрый день!\n"
            f"Недавно вы интересовались нашим роботом модели {robot.model}, версии {robot.version}.\n"
            f"Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами."
        )
        send_mail(
            subject,
            message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipient_list,
        )
