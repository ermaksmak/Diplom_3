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
    personal_account = PersonalAccountPage(browser)
    auth = AuthorizationsPage(browser)
    yield response, email, password, personal_account, auth

class TestPersonalAccount:

    @allure.title('Переход по клику на «Личный кабинет»')
    def test_personal_cabinet_navigation(self, browser, prepare_for_personal_account):
        _, _, _, personal_account, _ = prepare_for_personal_account
        with allure.step('Открываем главную страницу'):
            personal_account.open()
        with allure.step('Нажимаем на кнопку "Личный кабинет"'):
            personal_account.click_personal_account()
        with allure.step('Проверяем, что открылась страница авторизации'):
            assert personal_account.get_current_url() == f'{URL}{LOGIN}'

    @pytest.mark.usefixtures("prepare_for_personal_account")
    @allure.title('Переход в раздел «История заказов»')
    def test_navigate_to_order_history(self, browser, prepare_for_personal_account):
        _, email, password, personal_account, auth = prepare_for_personal_account
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            auth.login(email, password)
        with allure.step('Нажимаем на кнопку "Личный кабинет"'):
            personal_account.click_personal_account()
        with allure.step('Нажимаем на кнопку "История заказов"'):
            personal_account.click_button_history()
        with allure.step('Проверяем, что открылась страница "История заказов"'):
            assert personal_account.get_current_url() == f'{URL}{HISTORY}'

    @pytest.mark.usefixtures("prepare_for_personal_account")
    @allure.title('Выход из аккаунта')
    def test_logout_your_account(self, browser, prepare_for_personal_account):
        _, email, password, personal_account, auth = prepare_for_personal_account
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            auth.login(email, password)
        with allure.step('Нажимаем на кнопку "Личный кабинет"'):
            personal_account.click_personal_account()
        with allure.step('Нажимаем на кнопку "Выйти"'):
            personal_account.click_button_exit()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            personal_account.wait_for_page_load(f'{URL}{LOGIN}')
        with allure.step('Проверяем, что открылась страница авторизации'):
            assert personal_account.get_current_url() == f'{URL}{LOGIN}'