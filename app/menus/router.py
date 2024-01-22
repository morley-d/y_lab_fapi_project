from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from app.menus.dao import MenuDAO
from app.database import async_session_maker
from app.menus.shema import ShemaMenu, ShemaAddMenu

router = APIRouter(
    prefix="/api/v1/menus",
    tags=["Меню"]
)


@router.get("")
async def get_menus() -> list[ShemaMenu]:
    async with async_session_maker() as session:
        return await MenuDAO.find_all()


@router.get("/{menu_id}")
async def get_menu(menu_id) -> ShemaMenu:
    async with async_session_maker() as session:
        return await MenuDAO.find_one_or_none(id=int(menu_id))


@router.post("")
async def add_menu(menu_data: ShemaAddMenu):
    existing_menu = await MenuDAO.find_one_or_none(title=menu_data.title)
    if existing_menu:
        raise HTTPException(status_code=500)
    description = menu_data.description
    await MenuDAO.add(title=menu_data.title, description=description)
