from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.deps import get_db
from typing import List

from crud.crud_products import products_crud
from schemas.product import ProductCreate, ProductOut

router = APIRouter()

@router.get("",
            response_model=List[ProductOut],
            response_description="returns a list of new products",
            status_code=200,
            )
async def products(db: Session = Depends(get_db)):
    """
    Returns a list of all available products
    """
    products_list = products_crud.get_all_products(db=db)

    return products_list

@router.post("", 
            response_model=ProductOut,
            response_description="creates a new product",
            status_code=201,
    )
async def create_product(product_in: ProductCreate, db: Session = Depends(get_db)):
    """
    Adds a new product to the platform
    """
    try: 
        product = products_crud.create(db=db, obj_in=product_in)

        return product
    except Exception as e: 
        raise HTTPException(status_code=500, detail=f"{e}")