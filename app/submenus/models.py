from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Submenus(Base):
    __tablename__ = "submenus"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    menu_id = Column(Integer, ForeignKey("menus.id"))
