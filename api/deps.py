from typing import Optional

from fastapi import Header, Query

from core.auth import decode_access_token
from driver import sessions
from driver.driver import FirefoxPgeDriver, BaseDriver


def create_driver(_type: str = Query(None, alias='type')) -> Optional[BaseDriver]:
    if _type == 'pge':
        return FirefoxPgeDriver()

    return None


def get_current_user(authorization: Optional[str] = Header(None)) -> Optional[BaseDriver]:
    username = decode_access_token(authorization.split(' ')[1])

    return sessions.get(username)
