from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.movie import MovieCreate, MovieUpdate
from src.models import Movie


async def create_movie(session: AsyncSession, movie_data: MovieCreate) -> Movie:
    new_movie = Movie(**movie_data.model_dump())
    session.add(new_movie)
    await session.commit()
    return new_movie


async def get_movie(session: AsyncSession, movie_id: int) -> Movie | None:
    return await session.get(Movie, movie_id)

async def delete_movie(session: AsyncSession, movie_id) -> bool:
    movie_to_delete = await session.get(Movie, movie_id)
    if not movie_to_delete:
        return False
    await session.delete(movie_to_delete)
    await session.commit()
    return True
