from locators.order_feed_locator import number, completed_all_time
from locators.personal_account_locator import order_history_item
from pages.authorizations_page import AuthorizationsPage
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage
from url import URL, PROFILE
from pages.base_page import *
import pytest

@pytest.fixture()
def prepare_for_order(browser, create_and_delete_user):
    response, payload = create_and_delete_user
    email = payload['email']
    password = payload['password']
    order_history = PersonalAccountPage(browser)
    auth = AuthorizationsPage(browser)
    yield response, email, password, order_history, auth

class TestOrderFeed:

    @allure.title('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_open_order_details_popup(self, browser):
        order_details = OrderFeedPage(browser)
        with allure.step('Открываем главную страницу'):
            order_details.open()
        with allure.step('Нажимаем кнопку "Лента заказов"'):
            order_details.click_order_feed_button()
        with allure.step('Нажимаем на первый заказ в ленте'):
            order_details.click_order_history()
        with allure.step('Проверяем, что открылась окно с заказом'):
            assert order_details.get_popup_order_history().is_displayed()

    @allure.step('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_order_history_displayed_on_order_feed(self, browser, prepare_for_order):
        response, email, password, order_history, auth = prepare_for_order
        user_order_history = OrderFeedPage(browser)
        constructor = ConstructorPage(browser)
        personal_lk = PersonalAccountPage(browser)
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            auth.login(email, password)
        with allure.step('Добавляем ожидание для загрузки страницы с конструктором'):
            constructor.wait_for_page_load(f'{URL}')
        with allure.step('Собираем бургер и оформляем заказ'):
            constructor.create_burger_and_place_order()
        with allure.step('Добавляем ожидание для появления окна с заказом'):
            constructor.wait_loading_visibility(browser)
            constructor.wait_loading_invisibility(browser)
        with allure.step('Закрываем модальное окно с заказом'):
            constructor.get_close_modal_order()
        with allure.step('Нажимаем на кнопку "Личный кабинет"'):
            constructor.click_personal_account()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            constructor.wait_for_page_load(f'{URL}{PROFILE}')
        with allure.step('Нажимаем на кнопку "История заказов"'):
            personal_lk.click_button_history()
        with allure.step('Добавляем ожидание'):
            personal_lk.wait_for_order_history_item(order_history_item)
        with allure.step('Находим номер последнего заказа в ЛК'):
            last_order_number = personal_lk.get_order_history_item()
        with allure.step('Нажимаем кнопку "Лента заказов"'):
            user_order_history.click_order_feed_button()
        with allure.step('Добавляем ожидание'):
             personal_lk.wait_for_order_history_item(number)
        with allure.step('Проверяем, что последний заказ из ЛК есть в ленте заказов'):
            order_numbers_in_feed = user_order_history.get_order()
            assert last_order_number in order_numbers_in_feed


    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_orders_module_all_time_counter_increases(self, browser, prepare_for_order):
        response, email, password, order_history, auth = prepare_for_order
        orders_module_all_time = OrderFeedPage(browser)
        constructor = ConstructorPage(browser)
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            auth.login(email, password)
        with allure.step('Открываем страницу "Лента заказов"'):
            orders_module_all_time.click_order_feed_button()
        with allure.step('поиск счетчика заказов за все время'):
            orders_module_all_time.find(completed_all_time)
        with allure.step('Сохраняем кол-во заказов до создания нового'):
            count_number = orders_module_all_time.get_completed_all_time()
        with allure.step('Собираем бургер и оформляем заказ'):
            constructor.create_order_and_check_in_feed(browser)
        with allure.step('Проверяем, что новое значение не равно "count_number"'):
            assert orders_module_all_time.get_completed_all_time() != count_number


    @allure.title('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_create_new_order_increases_today_counter(self, browser, prepare_for_order):
        response, email, password, order_history, auth = prepare_for_order
        today_counter = OrderFeedPage(browser)
        constructor = ConstructorPage(browser)
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            auth.login(email, password)
        with allure.step('Добавляем ожидание для загрузки страницы с конструктором'):
            constructor.wait_for_page_load(f'{URL}')
        with allure.step('Открываем страницу "Лента заказов"'):
            today_counter.click_order_feed_button()
        with allure.step('Поиск счетчика заказов за сегодня'):
            today_counter.find(completed_all_time)
        with allure.step('Сохраняем кол-во заказов сегодня до создания нового'):
            count_number = today_counter.get_completed_today()
            constructor.create_order_and_check_in_feed(browser)
        with allure.step('Проверяем, что новое значение не равно "count_number"'):
            assert today_counter.get_completed_today() != count_number

    @allure.title('после оформления заказа его номер появляется в разделе "В работе".')
    def test_new_order_appears_in_work_section(self, browser, prepare_for_order):
        response, email, password, order_history, auth = prepare_for_order
        new_order_appears_in_work = OrderFeedPage(browser)
        constructor = ConstructorPage(browser)
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            auth.login(email, password)
        with allure.step('Добавляем ожидание для загрузки страницы с конструктором'):
            constructor.wait_for_page_load(f'{URL}')
        with allure.step('Собираем бургер и оформляем заказ'):
            constructor.create_burger_and_place_order()
        with allure.step('Добавляем ожидание для появления окна с заказом'):
            constructor.wait_loading_visibility(browser)
            constructor.wait_loading_invisibility(browser)
        with allure.step('Получаем номер заказа'):
            number_order ='0'+constructor.get_modal_order_text()
        with allure.step('Закрываем окно с заказом'):
            constructor.get_close_modal_order()
        with allure.step('Открываем страницу "Лента заказов"'):
            new_order_appears_in_work.click_order_feed_button()
        with allure.step('Получаем номер заказа в работе'):
            count_number = new_order_appears_in_work.get_at_work()
        with allure.step('Сравниваем, что номер заказа в работе совпадает с "number_order"'):
            assert count_number == number_order

