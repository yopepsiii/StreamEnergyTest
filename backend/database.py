from sqlalchemy import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from config import settings

SQLALCHEMY_DATABASE_URL = (
    f"postgresql:asyncpg"
    f"//{settings.database_username}"
    f":{settings.database_password}"
    f"@{settings.database_hostname}"
    f":{settings.database_port}"
    f"/{settings.database_name}"
)

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session
