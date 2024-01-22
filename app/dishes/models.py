from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Dishes(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    submenu_id = Column(Integer, ForeignKey("submenus.id"))
