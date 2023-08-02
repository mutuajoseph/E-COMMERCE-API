from sqlalchemy import Boolean, DateTime, func, String, Integer, Column
from db.base_class import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(length=256), nullable=False)
    last_name = Column(String(length=256), nullable=False)
    email = Column(String(length=256), nullable=False, unique=True)
    is_active = Column(Boolean, default=True, nullable=False)  # designates whether the user should be considered active
    password = Column(String(length=256), nullable=False)

    created = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)
    updated = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)