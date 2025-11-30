import asyncio
import pytest

from fastapi.testclient import TestClient
from sqlalchemy import StaticPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.main import app
from src.database import get_session
from src.models import Base, Movie


Movie_Test = []


@pytest.fixture(scope="session")
def test_engine():
    engine = create_async_engine("sqlite+aiosqlite:///:memory:", poolclass=StaticPool)
    yield engine
    asyncio.run(engine.dispose())


@pytest.fixture(scope="session")
def test_sessionmaker(test_engine):
    return async_sessionmaker(bind=test_engine)
