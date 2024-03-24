from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func
from datetime import datetime
from app.db.base import Base


class Url(Base):
    __tablename__ = 'urls'

    key: Mapped[str] = mapped_column(unique=True, index=True)
    target_url: Mapped[str] = mapped_column(index=True)
    clicks: Mapped[int] = mapped_column(default=0)
    created: Mapped[datetime] = mapped_column(server_default=func.now())
