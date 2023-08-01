from typing import Generator
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from settings.config import settings
from jose import JWTError, jwt
from crud.crud_user import user_crud

from requests import Session
from db.session import SessionLocal

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/user/login"
)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# get current user middleware -> to be injected to every route that needs to be guarded
async def get_current_user(db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid Credentials!",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError as e:
        raise HTTPException(status_code=401, detail=f'{e}')

    user = user_crud.get_by_id(db=db, id=user_id)

    if user is None:
        raise credentials_exception
    return user