from jobmatcher.services.cv_profile_service import process_cv
from jobmatcher.schemas.user import UserRead


def test_process_cv(db, cv_file):

    user = UserRead(
        id=1,
        email="donet@example.com",
        name="Donet",
        experience_years=2,
    )

    result = process_cv(
        db=db,
        path=str(cv_file),
        user=user
    )

    assert result is not None