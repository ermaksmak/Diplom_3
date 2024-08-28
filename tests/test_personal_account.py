import allure
import pytest
from pages.authorizations_page import AuthorizationsPage
from pages.personal_account_page import PersonalAccountPage
from url import URL, LOGIN, HISTORY

@pytest.fixture()
def prepare_for_personal_account(browser, create_and_delete_user):
    response, payload = create_and_delete_user
    email = payload['email']
    password = payload['password']
    order_history = PersonalAccountPage(browser)
    auth = AuthorizationsPage(browser)
    yield response, email, password, order_history, auth

class TestPersonalAccount:


    @allure.title('Переход по клику на «Личный кабинет»')
    def test_personal_cabinet_navigation(self, browser):
        personal_cabinet = PersonalAccountPage(browser)
        with allure.step('Открываем главную страницу'):
            personal_cabinet.open()
        with allure.step('Нажимаем на кнопку "Личный кабинет"'):
            personal_cabinet.click_personal_account()
        with allure.step('Проверяем, что открылась страница авторизации'):
            assert personal_cabinet.get_current_url() == f'{URL}{LOGIN}'

    @pytest.mark.usefixtures("prepare_for_personal_account")
    @allure.title('Переход в раздел «История заказов»')
    def test_navigate_to_order_history(self, browser, prepare_for_personal_account):
        response, email, password, order_history, auth = prepare_for_personal_account
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            auth.login(email, password)
        with allure.step('Нажимаем на кнопку "Личный кабинет"'):
            order_history.click_personal_account()
        with allure.step('Нажимаем на кнопку "История заказов"'):
            order_history.click_button_history()
        with allure.step('Проверяем, что открылась страница "История заказов"'):
            assert order_history.get_current_url() == f'{URL}{HISTORY}'

    @pytest.mark.usefixtures("prepare_for_personal_account")
    @allure.title('Выход из аккаунта')
    def test_logout_your_account(self, browser, prepare_for_personal_account):
        response, email, password, logout_your, auth = prepare_for_personal_account
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            auth.login(email, password)
        with allure.step('Нажимаем на кнопку "Личный кабинет"'):
            logout_your.click_personal_account()
        with allure.step('Нажимаем на кнопку "Выйти"'):
            logout_your.click_button_exit()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            logout_your.wait_for_page_load(f'{URL}{LOGIN}')
        with allure.step('Проверяем, что открылась страница авторизации'):
            assert logout_your.get_current_url() == f'{URL}{LOGIN}'