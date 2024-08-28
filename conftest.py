import requests
from selenium import webdriver
import pytest
import sys
import os
from helpers import generate_user_data
from url import URL, CREATE_USER, DELETE_USER
from selenium.webdriver.chrome.service import Service


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
