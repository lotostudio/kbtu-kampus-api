from typing import Dict

from fastapi import APIRouter, Depends
from selenium.webdriver.remote.webdriver import WebDriver

from api.deps import create_driver, get_current_user
from core.auth import create_access_token
from driver import sessions, driver
from schemas import Token, ToLogin

router = APIRouter()

ma: Dict[str, WebDriver] = {}


@router.post('/login')
def login(to_login: ToLogin, d: driver.BaseDriver = Depends(create_driver)) -> Token:
    d.login(to_login.username, to_login.password)

    token = create_access_token(to_login.username)

    sessions.put(to_login.username, d)

    return Token(access_token=token, type='bearer')


@router.get('/news')
def news(d: driver.BaseDriver = Depends(get_current_user)) -> str:
    return d.news()
