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
    Token,
    UserCreate,
    UserLogin,
    UserRead,
)
from jobmatcher.services.auth_service import (
    authenticate_user,
    create_access_token,
    create_user,
    get_user_by_email,
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
            detail="Email already registered",
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
            detail="Invalid email or password",
        )

    token = create_access_token(
        user.id
    )

    return Token(
        access_token=token,
        token_type="bearer",
    )