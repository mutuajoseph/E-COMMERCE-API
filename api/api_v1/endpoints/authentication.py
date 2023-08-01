from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.deps import get_db
from crud.crud_user import user_crud
from models.users import Users
from schemas.user import UserOut, UserCreate
from schemas.login import Token
from utils.security import create_access_token, verify_password
from settings.config import settings

router = APIRouter()


@router.post("/signup",
             response_model=UserOut,
             response_description="creates a new user",
             status_code=201,
             )
async def signup(user_in: UserCreate, db: Session = Depends(get_db)):
    """
    Adds a non existent user to the database
    """
    try:
        new_user = user_crud.create(obj_in=user_in, db=db)
        return new_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'{e}')


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    OAuth2 compatible token login, get an access token for future requests
    """

    try:
        # check whether the user exists
        user = db.query(Users).filter(Users.email == form_data.username).first()
        if not user:
            raise HTTPException(status_code=401, detail="Invalid Credentials")

        # compare the two passwords
        if not verify_password(form_data.password, hashed_password=user.password):
            raise HTTPException(status_code=401, detail="Invalid Credentials")

        # check whether the account is active
        if not user.is_active:
            raise HTTPException(status_code=401, detail="User Account has been deactivated! Contact Support")

        # generate a JWT token
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token_expires_in_milliseconds = settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
        access_token = create_access_token(user.id, access_token_expires)

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": access_token_expires_in_milliseconds,
            "user": user
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'{e}')