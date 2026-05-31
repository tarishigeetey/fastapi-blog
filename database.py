from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"  # Database URL for SQLite, using a local file named blog.db

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)  # Create a SQLAlchemy engine with the specified database URL and connection arguments

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)  # Create a session factory that will be used to create database sessions


class Base(DeclarativeBase):
    pass  # Base class for all ORM


async def get_DB():
    async with (
        AsyncSessionLocal() as session
    ):  # Create a new database session using the session factory
        yield session  # Yield the database session for use in API endpoints, ensuring proper cleanup after use
