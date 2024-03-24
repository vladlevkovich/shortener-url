from typing import Annotated
from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.db import get_db
from app.schemas.schema import BaseUrl
from app.services.urls_services import create_url, get_all_links, click_url, popular_urls

router = APIRouter()
templates = Jinja2Templates(directory='app/templates')


@router.get('/target/{url_key}')
async def get_url(url_key: str, db: AsyncSession = Depends(get_db)):
    return await click_url(db=db, url_key=url_key)


@router.get('/popular')
async def get_popular_urls(request: Request, db: AsyncSession = Depends(get_db)):
    links = await popular_urls(db=db)
    return templates.TemplateResponse('links.html', {'request': request, 'links': links})


@router.get('/url', response_class=HTMLResponse)
async def list_urls(request: Request, db: AsyncSession = Depends(get_db)):
    links = await get_all_links(db=db)
    return templates.TemplateResponse('links.html', {'request': request, 'links': links})


@router.get('/create')
async def create_url_page(request: Request):
    return templates.TemplateResponse('create_url.html', {'request': request})


@router.post('/new')
async def add_url(request: Request, orig_url: Annotated[str, Form()], db: AsyncSession = Depends(get_db)):
    try:
        data = BaseUrl(target_url=orig_url)
        new_url = await create_url(orig_ulr=orig_url, db=db)
        return templates.TemplateResponse('create_url.html', {'request': request, 'new_url': new_url})
    except Exception as e:
        print(str(e))
        return {'message': str(e)}
