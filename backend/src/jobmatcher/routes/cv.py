import uuid
from pathlib import Path

import aiofiles
from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    HTTPException,
    UploadFile,
)
from sqlalchemy.orm import Session

from jobmatcher.auth.dependencies import get_current_user
from jobmatcher.database.dependencies import get_db
from jobmatcher.models.user import User
from jobmatcher.services.cv_profile_service import process_cv


router = APIRouter(
    prefix="/cv",
    tags=["CV"],
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

MAX_FILE_SIZE = 10 * 1024 * 1024

ALLOWED_FILE_TYPES = {
    ".pdf": {
        "application/pdf",
    },
    ".docx": {
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    },
}


@router.post("/upload")
async def upload_cv(
    name: str | None = Form(None),
    experience_years: float | None = Form(None),
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is missing.",
        )

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are supported.",
        )

    if file.content_type not in ALLOWED_FILE_TYPES[extension]:
        raise HTTPException(
            status_code=400,
            detail="File content type does not match its extension.",
        )

    content = await file.read(
        MAX_FILE_SIZE + 1
    )

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="File is too large. Maximum size is 10 MB.",
        )

    safe_filename = f"{uuid.uuid4()}{extension}"
    file_path = UPLOAD_DIR / safe_filename

    try:
        async with aiofiles.open(
            file_path,
            "wb",
        ) as buffer:
            await buffer.write(content)

        try:
            profile, _ = process_cv(
                db=db,
                user=current_user,
                path=file_path,
            )
        except Exception as exc:
            raise HTTPException(
                status_code=400,
                detail="Unable to process the uploaded CV.",
            ) from exc

        return {
            "message": "CV processed successfully",
            "profile": profile,
        }

    finally:
        if file_path.exists():
            file_path.unlink()