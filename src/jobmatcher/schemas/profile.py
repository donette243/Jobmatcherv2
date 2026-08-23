from pydantic import BaseModel, Field


class PreferenceCreate(BaseModel):
    desired_position: str | None = None
    desired_location: str | None = None
    remote: bool = False
    min_salary: float | None = Field(
        default=None,
        ge=0,
    )


class PreferenceRead(PreferenceCreate):
    id: int

    model_config = {
        "from_attributes": True
    }


class ProfileCreate(BaseModel):
    name: str | None = None
    experience_years: float | None = Field(
        default=None,
        ge=0,
    )
    preference: PreferenceCreate | None = None


class ProfileRead(BaseModel):
    id: int
    user_id: int
    name: str | None
    experience_years: float | None
    skills: list[str] = []
    preference: PreferenceRead | None = None
    languages: list[str] = []
    education: list[str] = []
    desired_positions: list[str] = []

    model_config = {
        "from_attributes": True
    }


class ProfileExtract(BaseModel):
    name: str | None
    experience_years: float | None
    skills: list[str]
    languages: list[str]
    education: list[str]
    desired_positions: list[str]

    model_config = {
        "from_attributes": True
    }