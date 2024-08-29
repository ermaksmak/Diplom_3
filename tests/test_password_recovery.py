import allure
import pytest
from pages.password_recovery_page import PasswordRecoveryPage
from url import LOGIN
from url import URL, RESET_PASSWORD, FORGOT_PASSWORD

@pytest.fixture()
def prepare_for_recovery_password(browser):
    recovery_page = PasswordRecoveryPage(browser)
    yield recovery_page
class TestPasswordRecovery:

    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль»,')
    def test_password_recovery_page(self, browser, prepare_for_recovery_password):
        recovery_page = prepare_for_recovery_password
        with allure.step('Открываем страницу авторизации'):
            recovery_page.open(f'{URL}{LOGIN}')
        with allure.step('Нажимаем на кнопку "Восстановить пароль"'):
            recovery_page.click_button_password_recovery()
        with allure.step('Проверяем, что открылась страница восстановления пароля'):
            assert recovery_page.get_current_url() == f'{URL}{FORGOT_PASSWORD}'

    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    def test_password_reset_email_submission(self, browser, prepare_for_recovery_password):
        recovery_page = prepare_for_recovery_password
        with allure.step('Открываем страницу авторизации'):
            recovery_page.open(f'{URL}{FORGOT_PASSWORD}')
        with allure.step('Вводим почту'):
            recovery_page.send_keys_email_input_recovery_password()
        with allure.step('Нажимаем кнопку "Восстановить"'):
            recovery_page.click_button_recovery()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            recovery_page.wait_for_page_load(f'{URL}{RESET_PASSWORD}')
        with allure.step('Проверяем, что открылась страница восстановления пароля'):
            assert recovery_page.get_current_url() == f'{URL}{RESET_PASSWORD}'


    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_show_activates_password_field(self, browser, prepare_for_recovery_password):
        recovery_page = prepare_for_recovery_password
        with allure.step('Открываем страницу авторизации'):
            recovery_page.open(f'{URL}{LOGIN}')
        with allure.step('Нажимаем на кнопку "Восстановить пароль"'):
            recovery_page.click_button_password_recovery()
        with allure.step('Вводим почту'):
            recovery_page.send_keys_email_input_recovery_password()
        with allure.step('Нажимаем кнопку "Восстановить"'):
            recovery_page.click_button_recovery()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            recovery_page.wait_for_page_load(f'{URL}{RESET_PASSWORD}')
        with allure.step('Нажимает на кнопку "Показать/Скрыть" пароль'):
            recovery_page.show_hide_button_click()
        with allure.step('Проверяем, что поле пароля активно'):
            assert 'input_status_active' in recovery_page.get_show_password().get_attribute('class')
