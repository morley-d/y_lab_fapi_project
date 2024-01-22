from app.menus.models import Menus
from dao.base import BaseDAO


class MenuDAO(BaseDAO):
    model = Menus
