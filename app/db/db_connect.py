from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.core import settings


class Database:
    def __init__(self):
        self.engine = create_async_engine(url=settings.DB_URL, echo=True)
        self.session = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )


db = Database()
