from sqlalchemy import Boolean, DateTime, func, String, Integer, Column
from db.base_class import Base

class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(length=256), nullable=False)
    product_description = Column(String(length=256), nullable=False)
    unit_price = Column(Integer, nullable=False)
    ranking = Column(Integer, nullable=False)
    product_full_image = Column(String(), nullable=False)
    product_thumbnail = Column(String(), nullable=False)

    created = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)
    updated = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
