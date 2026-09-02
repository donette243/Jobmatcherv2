import os
import smtplib
from email.message import EmailMessage


SMTP_HOST = os.getenv(
    "SMTP_HOST",
    "smtp.gmail.com",
)

SMTP_PORT = int(
    os.getenv(
        "SMTP_PORT",
        "587",
    )
)

SMTP_USER = os.getenv("SMTP_USER")

SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

SMTP_FROM = os.getenv(
    "SMTP_FROM",
    SMTP_USER,
)

FRONTEND_URL = os.getenv(
    "FRONTEND_URL",
    "http://localhost:5173",
)


def send_password_reset_email(
    recipient_email: str,
    token: str,
) -> None:
    reset_link = (
        f"{FRONTEND_URL}/reset-password?token={token}"
    )

    message = EmailMessage()

    message["Subject"] = (
        "Восстановление пароля — JobMatcher"
    )

    message["From"] = SMTP_FROM
    message["To"] = recipient_email

    message.set_content(
        f"""Здравствуйте!

Вы запросили восстановление пароля для вашего аккаунта JobMatcher.

Чтобы установить новый пароль, перейдите по ссылке:

{reset_link}

Ссылка действительна в течение 30 минут.

Если вы не запрашивали восстановление пароля, просто проигнорируйте это письмо.

С уважением,
Команда JobMatcher
"""
    )

    with smtplib.SMTP(
        SMTP_HOST,
        SMTP_PORT,
    ) as server:
        server.starttls()

        server.login(
            SMTP_USER,
            SMTP_PASSWORD,
        )

        server.send_message(message)