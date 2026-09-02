from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from jobmatcher.database.dependencies import get_db
from jobmatcher.schemas.auth import (
    ForgotPasswordRequest,
    ResetPasswordRequest,
    Token,
    UserCreate,
    UserLogin,
    UserRead,
)
from jobmatcher.services.auth_service import (
    authenticate_user,
    create_access_token,
    create_password_reset_token,
    create_user,
    get_user_by_email,
    get_user_by_reset_token,
    reset_user_password,
)
from jobmatcher.services.email_service import (
    send_password_reset_email,
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
def register(
    data: UserCreate,
    db: Annotated[
        Session,
        Depends(get_db),
    ],
):
    existing_user = get_user_by_email(
        db,
        data.email,
    )

    if existing_user is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Этот email уже зарегистрирован",
        )

    return create_user(
        db,
        data.email,
        data.password,
    )


@router.post(
    "/login",
    response_model=Token,
)
def login(
    data: UserLogin,
    db: Annotated[
        Session,
        Depends(get_db),
    ],
):
    user = authenticate_user(
        db,
        data.email,
        data.password,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный email или пароль",
        )

    token = create_access_token(
        user.id
    )

    return Token(
        access_token=token,
        token_type="bearer",
    )


@router.post(
    "/forgot-password",
)
def forgot_password(
    data: ForgotPasswordRequest,
    db: Annotated[
        Session,
        Depends(get_db),
    ],
):
    user = get_user_by_email(
        db,
        data.email,
    )

    if user is not None:
        token = create_password_reset_token(
            db,
            user,
        )

        send_password_reset_email(
            user.email,
            token,
        )

    return {
        "message": (
            "Если аккаунт с таким email существует, "
            "ссылка для восстановления пароля будет отправлена."
        )
    }


@router.post(
    "/reset-password",
)
def reset_password(
    data: ResetPasswordRequest,
    db: Annotated[
        Session,
        Depends(get_db),
    ],
):
    user = get_user_by_reset_token(
        db,
        data.token,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Ссылка для восстановления пароля "
                "недействительна или истекла"
            ),
        )

    reset_user_password(
        db,
        user,
        data.new_password,
    )

    return {
        "message": "Пароль успешно изменён",
    }