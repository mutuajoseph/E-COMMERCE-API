# will place all endpoints that relate to api version one

from fastapi import APIRouter
from api.api_v1.endpoints import (authentication, products)

# router instance
api_router = APIRouter()

api_router.include_router(authentication.router, prefix="/user", tags=["E-COMMERCE AUTHENTICATION"])
api_router.include_router(products.router, prefix="/products", tags=["E-COMMERCE PRODUCTS"])
