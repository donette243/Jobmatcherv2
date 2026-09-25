import os

from dotenv import load_dotenv


load_dotenv()


def _required_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise RuntimeError(
            f"{name} is not configured. "
            f"Create a .env file and define {name}."
        )

    return value


DATABASE_URL = _required_env("DATABASE_URL")
JWT_SECRET_KEY = _required_env("JWT_SECRET_KEY")

JWT_ALGORITHM = os.getenv(
    "JWT_ALGORITHM",
    "HS256",
)

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES",
        "60",
    )
)

RESET_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        "RESET_TOKEN_EXPIRE_MINUTES",
        "30",
    )
)

SMTP_HOST = os.getenv(
    "SMTP_HOST",
    "localhost",
)

SMTP_PORT = int(
    os.getenv(
        "SMTP_PORT",
        "1025",
    )
)

SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

SMTP_FROM = os.getenv(
    "SMTP_FROM",
    "jobmatcher@example.com",
)

SMTP_USE_TLS = (
    os.getenv(
        "SMTP_USE_TLS",
        "false",
    ).lower()
    == "true"
)

FRONTEND_URL = os.getenv(
    "FRONTEND_URL",
    "http://localhost:5173",
)