from app.database import Base
from sqlalchemy import Column, Integer, String


class Menus(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
