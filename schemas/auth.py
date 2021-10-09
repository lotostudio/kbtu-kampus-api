from typing import Optional

from pydantic import BaseModel


class ToLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    type: str


class TokenPayload(BaseModel):
    sub: Optional[str] = None
