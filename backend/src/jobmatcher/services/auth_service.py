import os
import secrets
from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.orm import Session

from jobmatcher.models.user import User


password_hash = PasswordHash.recommended()

JWT_SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY",
    "change-this-secret-key",
)

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


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(
    password: str,
    hashed_password: str,
) -> bool:
    return password_hash.verify(
        password,
        hashed_password,
    )


def get_user_by_email(
    db: Session,
    email: str,
) -> User | None:
    statement = select(User).where(
        User.email == email
    )

    return db.scalar(statement)


def create_user(
    db: Session,
    email: str,
    password: str,
) -> User:
    user = User(
        email=email,
        password_hash=hash_password(password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def authenticate_user(
    db: Session,
    email: str,
    password: str,
) -> User | None:
    user = get_user_by_email(
        db,
        email,
    )

    if user is None:
        return None

    if not verify_password(
        password,
        user.password_hash,
    ):
        return None

    return user


def create_access_token(
    user_id: int,
) -> str:
    expires_at = (
        datetime.now(timezone.utc)
        + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    payload = {
        "sub": str(user_id),
        "exp": expires_at,
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )


def decode_access_token(
    token: str,
) -> int:
    payload = jwt.decode(
        token,
        JWT_SECRET_KEY,
        algorithms=[JWT_ALGORITHM],
    )

    return int(payload["sub"])


def create_password_reset_token(
    db: Session,
    user: User,
) -> str:
    token = secrets.token_urlsafe(32)

    user.reset_token = token
    user.reset_token_expires_at = (
        datetime.now(timezone.utc)
        + timedelta(
            minutes=RESET_TOKEN_EXPIRE_MINUTES
        )
    )

    db.commit()

    return token


def get_user_by_reset_token(
    db: Session,
    token: str,
) -> User | None:
    statement = select(User).where(
        User.reset_token == token
    )

    user = db.scalar(statement)

    if user is None:
        return None

    if user.reset_token_expires_at is None:
        return None

    expires_at = user.reset_token_expires_at

    if expires_at.tzinfo is None:
        expires_at = expires_at.replace(
            tzinfo=timezone.utc
        )

    if datetime.now(timezone.utc) > expires_at:
        return None

    return user


def reset_user_password(
    db: Session,
    user: User,
    new_password: str,
) -> None:
    user.password_hash = hash_password(
        new_password
    )

    user.reset_token = None
    user.reset_token_expires_at = None

    db.commit()