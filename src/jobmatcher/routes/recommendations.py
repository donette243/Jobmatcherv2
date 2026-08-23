from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
)
from sqlalchemy.orm import Session

from jobmatcher.auth.dependencies import (
    get_current_user,
)
from jobmatcher.database.dependencies import (
    get_db,
)
from jobmatcher.models.user import User
# from jobmatcher.services.job_service import (
#     get_jobs,
# )
from jobmatcher.services.profile_service import (
    get_profile,
)
from jobmatcher.services.recommendation_service import (
    get_recommendations,
)


router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"],
)


@router.get("")
def recommendations(
    db: Annotated[
        Session,
        Depends(get_db),
    ],
    user: Annotated[
        User,
        Depends(get_current_user),
    ],
    limit: int = Query(
        default=10,
        ge=1,
        le=100,
    ),
):
    profile = get_profile(
        db,
        user.id,
    )

    if profile is None:
        raise HTTPException(
            status_code=404,
            detail="Profile not found",
        )

    # jobs = get_jobs(db)

    return get_recommendations(
        db,
        profile_id=profile.id,
        # limit=limit,
    )