from datetime import datetime
from typing import Optional, AnyStr
from pydantic import BaseModel

class ProductBase(BaseModel):
    product_name: str
    product_description: str
    unit_price: int
    product_full_image: str
    product_thumbnail: str
    ranking: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductCreate):
    pass

class ProductOut(ProductBase):
    created: Optional[datetime]
    updated: Optional[datetime]

    class Config:
        orm_mode = True
        