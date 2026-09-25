from jobmatcher.models.user import User
from jobmatcher.services.cv_profile_service import process_cv
def test_process_cv(db, cv_file):
    user = User(
        email="donet@example.com",
        password_hash="test-password-hash",
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    profile, parsed = process_cv(
        db=db,
        path=str(cv_file),
        user=user,
    )

    assert profile is not None
    assert profile.id is not None
    assert profile.user_id == user.id
    assert parsed is not None
    assert isinstance(parsed, str)
    assert len(parsed.strip()) > 0