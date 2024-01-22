from fastapi import APIRouter
from sqlalchemy import select
from app.menus.dao import MenuDAO
from app.database import async_session_maker
from app.menus.shema import ShemaMenu

router = APIRouter(
    prefix="/api/v1/menus",
    tags=["Меню"]
)


@router.get("")
async def get_menus() -> list[ShemaMenu]:
    async with async_session_maker() as session:
        return await MenuDAO.find_all()

# @router.get("/{booking_id}")
# def get_booking(booking_id):
#     pass
