import requests
from selenium import webdriver
import pytest
import sys
import os
from helpers import generate_user_data
from url import URL, CREATE_USER, DELETE_USER
from selenium.webdriver.chrome.service import Service
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage
from pages.authorizations_page import AuthorizationsPage
from pages.personal_account_page import PersonalAccountPage
from pages.password_recovery_page import PasswordRecoveryPage


# Добавляем путь к директории "pages"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        service = Service()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(service=service, options=chrome_options)
    elif request.param == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise TypeError("Driver is not found")
    driver.get(URL)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def create_and_delete_user():
    """
    Фикстура для создания и удаления пользователя.
    """
    payload = generate_user_data()
    response = requests.post(URL + CREATE_USER, json=payload)
    yield response, payload
    access_token = response.json()['accessToken']
    requests.delete(URL + DELETE_USER, headers={'Authorization': access_token})

@pytest.fixture
def prepare_for_constructor(browser, create_and_delete_user):
    response, payload = create_and_delete_user
    email = payload['email']
    password = payload['password']
    auth = AuthorizationsPage(browser)
    constructor = ConstructorPage(browser)
    order_feed_page = OrderFeedPage(browser)
    yield response, email, password, auth, constructor, order_feed_page

@pytest.fixture()
def prepare_for_order(browser, create_and_delete_user):
    response, payload = create_and_delete_user
    email = payload['email']
    password = payload['password']
    auth = AuthorizationsPage(browser)
    order_feed_page = OrderFeedPage(browser)
    personal_account = PersonalAccountPage(browser)
    constructor = ConstructorPage(browser)
    yield response, email, password, auth, order_feed_page, personal_account, constructor

@pytest.fixture()
def prepare_for_recovery_password(browser):
    recovery_page = PasswordRecoveryPage(browser)
    yield recovery_page

@pytest.fixture()
def prepare_for_personal_account(browser, create_and_delete_user):
    response, payload = create_and_delete_user
    email = payload['email']
    password = payload['password']
    personal_account = PersonalAccountPage(browser)
    auth = AuthorizationsPage(browser)
    yield response, email, password, personal_account, auth