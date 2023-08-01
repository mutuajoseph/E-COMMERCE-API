from typing import Any, Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.users import Users
from schemas.user import UserCreate, UserUpdate
from utils.security import get_password_hash
from crud.base import CRUDBase


class CRUDUser(CRUDBase[Users, UserCreate, UserUpdate]):

    def get_by_id(self, db: Session, id: Any) -> Optional[Users]:

        # Check whether the user exists
        user = db.query(Users).filter(Users.id == id).first()

        if user is None:
            raise HTTPException(status_code=404, detail=f"user with the id {id} does not exist")

        return user

    def get_by_email(self, db: Session, *, email: str) -> Optional[Users]:

        user = db.query(Users).filter(Users.email == email).first()

        if user is None:
            raise HTTPException(status_code=404, detail=f"user with email {email} does not exist")

        return user

    def create(self, db: Session, *, obj_in: UserCreate) -> Users:

        # check whether the email exists
        user = db.query(Users).filter(Users.email == obj_in.email).first()

        if user:
            raise HTTPException(status_code=400, detail="user with such an email already exists")

        usr_obj = Users(
            first_name=obj_in.first_name.title(),
            last_name=obj_in.last_name.title(),
            email=obj_in.email.lower(),
            password=obj_in.password,
        )

        # get the password and hash it
        hashed_password = get_password_hash(usr_obj.password)

        # create the new user object
        usr_obj.password = hashed_password

        # save the record on a db
        db.add(usr_obj)
        db.commit()
        db.refresh(usr_obj)
        return usr_obj


user_crud = CRUDUser(Users)