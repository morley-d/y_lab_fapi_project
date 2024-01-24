from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel
from app.menus.router import router as router_menus


app = FastAPI()

app.include_router(router_menus)


class HotelSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        stars: Optional[int] = Query(None, ge=1, le=5),
        has_spa: Optional[bool] = None
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


class ShemaHotel(BaseModel):
    adress: str
    name: str
    stars: int


@app.get("/submenus/")
def get_submenus(
    search_args: HotelSearchArgs = Depends()
):
    hotels = [
        {
            "adress": "ул.Гагарина, 1, Алтай",
            "name": "Super Hotel",
            "stars": 5
        }
    ]
    return hotels


class ShemaBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date
