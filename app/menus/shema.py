from pydantic import BaseModel


class ShemaMenu(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True


class ShemaAddMenu(BaseModel):
    title: str
    description: str
