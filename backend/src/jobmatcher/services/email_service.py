import smtplib
from email.message import EmailMessage

from jobmatcher.config import (
    FRONTEND_URL,
    RESET_TOKEN_EXPIRE_MINUTES,
    SMTP_FROM,
    SMTP_HOST,
    SMTP_PASSWORD,
    SMTP_PORT,
    SMTP_USER,
    SMTP_USE_TLS,
)


def send_password_reset_email(
    recipient_email: str,
    token: str,
) -> None:
    reset_link = (
        f"{FRONTEND_URL}/reset-password"
        f"?token={token}"
    )

    message = EmailMessage()
    message["Subject"] = "Восстановление пароля — JobMatcher"
    message["From"] = SMTP_FROM
    message["To"] = recipient_email

    message.set_content(
        f"""Здравствуйте!

Вы запросили восстановление пароля для вашего аккаунта JobMatcher.

Чтобы установить новый пароль, перейдите по ссылке:

{reset_link}

Ссылка действительна в течение {RESET_TOKEN_EXPIRE_MINUTES} минут.

Если вы не запрашивали восстановление пароля, просто проигнорируйте это письмо.

С уважением,
Команда JobMatcher
"""
    )

    with smtplib.SMTP(
        SMTP_HOST,
        SMTP_PORT,
    ) as server:
        if SMTP_USE_TLS:
            server.starttls()

        if SMTP_USER and SMTP_PASSWORD:
            server.login(
                SMTP_USER,
                SMTP_PASSWORD,
            )

        server.send_message(message)