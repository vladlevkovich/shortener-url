from fastapi import HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from app.models.models import Url
from app.schemas.schema import BaseUrl
import secrets


async def get_all_links(db: AsyncSession):
    links = await db.scalars(select(Url))
    return links.all()


async def popular_urls(db: AsyncSession):
    stmt = select(Url).order_by(desc(Url.clicks))
    result = await db.scalars(stmt)
    return result.all()


async def click_url(url_key: str, db: AsyncSession):
    url = await db.scalar(select(Url).where(Url.key == url_key))
    if not url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Url not found'
        )
    url.clicks += 1
    await db.commit()
    return RedirectResponse(url.target_url)


async def create_url(orig_ulr, db: AsyncSession):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = ''.join(secrets.choice(chars) for _ in range(5))
    url = Url(
        key=key,
        target_url=orig_ulr
    )
    db.add(url)
    await db.commit()
    return url

