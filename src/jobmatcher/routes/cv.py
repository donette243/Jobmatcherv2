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
from jobmatcher.database.database import SessionLocal
from jobmatcher.models.user import User
from jobmatcher.services.cv_profile_service import process_cv

router = APIRouter(
    prefix="/cv",
    tags=["CV"],
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
}


@router.post("/upload")
async def upload_cv(
    name: str | None = Form(None),
    experience_years: float | None = Form(None),
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is missing.",
        )

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are supported.",
        )

    safe_filename = f"{uuid.uuid4()}{extension}"
    file_path = UPLOAD_DIR / safe_filename

    content = await file.read()

    async with aiofiles.open(file_path, "wb") as buffer:
        await buffer.write(content)

    db: Session = SessionLocal()

    try:
        result = process_cv(
            db=db,
            user=current_user,
            path=str(file_path),
        )

        return {
            "message": "CV processed successfully",
            "profile": result,
        }

    finally:
        db.close()