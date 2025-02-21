from pydantic import BaseModel


class RentDataSchema(BaseModel):
    id: int
    neighborhood: str
    rent_price: int

    class Config:
        from_attributes = True  # ✅ Allows conversion from SQLAlchemy model
