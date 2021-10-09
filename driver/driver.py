import abc
import time
from typing import Dict

from selenium import webdriver

from core.config import settings


class BaseDriver(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def login(self, username: str, password: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def news(self) -> str:
        raise NotImplementedError


class DriverSessions:

    def __init__(self):
        self.sessions: Dict[str, BaseDriver] = {}

    def get(self, token: str) -> BaseDriver:
        return self.sessions.get(token)

    def put(self, token: str, driver: BaseDriver) -> None:
        self.sessions[token] = driver


sessions = DriverSessions()


class FirefoxPgeDriver(BaseDriver):

    MAIN_URL = settings.POSTGRADUATE_PORTAL_URL

    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')

        self.driver = webdriver.Firefox(options=options)

    def login(self, username: str, password: str) -> None:
        self.driver.get(self.MAIN_URL)
        time.sleep(1)

        elem = self.driver.find_element_by_class_name("v-align-right")
        x = elem.find_element_by_class_name('v-icon')
        x.click()
        time.sleep(1)

        usernameEl = self.driver.find_element_by_id('gwt-uid-4')
        usernameEl.send_keys(username)
        time.sleep(0.5)
        passwordEl = self.driver.find_element_by_id('gwt-uid-6')
        passwordEl.send_keys(password)

        login_page = self.driver.find_element_by_class_name('v-button-primary')
        login_page.click()

        self.go_home()

    def news(self) -> str:
        self.driver.get(f'{self.MAIN_URL}/News')
        time.sleep(1)
        return self.driver.page_source

    def go_home(self):
        time.sleep(1)
        button = self.driver.find_element_by_class_name('v-slot-icon-only')
        button.click()
