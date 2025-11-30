from datetime import date
from pydantic import BaseModel, Field, ConfigDict, field_validator


class MovieBase(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    genre: str = Field(min_length=2, max_length=50)
    rating: float = Field(ge=0, le=10)
    year: int

    @field_validator("year")
    @classmethod
    def validate_year(cls, year: int) -> int:
        if not(1900 <= year <= date.today().year):
            raise ValueError(f"year must be between 1900 and {date.today().year}")
        return year


class MovieCreate(MovieBase):
    pass


class MovieUpdate(MovieBase):
    title: str | None = Field(default=None, min_length=2, max_length=100)
    genre: str | None = Field(default=None, min_length=2, max_length=50)
    rating: float | None = Field(default=None, ge=0, le=10)
    year: int | None = None


class MovieOut(MovieBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
