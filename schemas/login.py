from typing import Any, Optional

from pydantic import BaseModel

from .user import UserOut


class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserOut
    expires_in: Optional[Any]


class TokenPayload(BaseModel):
    sub: Optional[int] = None