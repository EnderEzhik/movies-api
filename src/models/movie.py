from sqlalchemy import Column, Integer, String, Float, CheckConstraint
from . import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    year = Column(Integer, nullable=False)
    genre = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
    description = Column(String, nullable=False)

    __table__args__ = (CheckConstraint("rating >= 0 AND rating <= 10"),
                       CheckConstraint("year >= 1900", name="check_movie_year_ge_1900"))
