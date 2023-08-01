from email.mime import image
from optparse import Option
from typing import Any, Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.products import Products
from schemas.product import ProductCreate, ProductOut
from crud.base import CRUDBase


class CRUDProduct(CRUDBase[Products, ProductCreate, ProductOut]):

    def get_by_id(self, db: Session, id: Any) -> Optional[Products]:

        # check whether the product exists
        product = db.query(Products).filter(Products.id == id).first()

        if product is None:
            raise HTTPException(status_code=404, detail=f"product with the id {id} does not exist")

        return product

    def get_all_products(self, db: Session) -> Optional[Products]:

        try: 
            products = db.query(Products).all()

            return products
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'{e}')


    def create(self, db: Session, *, obj_in: ProductCreate) -> Products:

        product_obj = Products(
            product_name = obj_in.product_name.title(),
            product_description = obj_in.product_description.title(),
            unit_price = obj_in.unit_price,
            ranking = obj_in.ranking,
            product_full_image = obj_in.product_full_image,
            product_thumbnail = obj_in.product_thumbnail
        )

        db.add(product_obj)
        db.commit()
        db.refresh(product_obj)
        return product_obj

products_crud = CRUDProduct(Products)