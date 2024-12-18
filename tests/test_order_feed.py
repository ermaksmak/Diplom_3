from locators.order_feed_locator import number, completed_all_time
from locators.personal_account_locator import order_history_item
from url import URL, PROFILE
from pages.base_page import *
import allure




class TestOrderFeed:

    @allure.title('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_open_order_details_popup(self, browser, prepare_for_order):
        _, _, _, _,order_feed_page, _, _ = prepare_for_order
        with allure.step('Открываем главную страницу'):
            order_feed_page.open()
        with allure.step('Нажимаем кнопку "Лента заказов"'):
            order_feed_page.click_order_feed_button()
        with allure.step('Нажимаем на первый заказ в ленте'):
            order_feed_page.click_order_history()
        with allure.step('Проверяем, что открылась окно с заказом'):
            assert order_feed_page.get_popup_order_history().is_displayed()

    @allure.step('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_order_history_displayed_on_order_feed(self, browser, prepare_for_order):
        _, email, password, auth, order_feed_page, personal_account, constructor = prepare_for_order
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
            personal_account.click_button_history()
        with allure.step('Добавляем ожидание'):
            personal_account.wait_for_order_history_item(order_history_item)
        with allure.step('Находим номер последнего заказа в ЛК'):
            last_order_number = personal_account.get_order_history_item()
        with allure.step('Нажимаем кнопку "Лента заказов"'):
            order_feed_page.click_order_feed_button()
        with allure.step('Добавляем ожидание'):
             personal_account.wait_for_order_history_item(number)
        with allure.step('Проверяем, что последний заказ из ЛК есть в ленте заказов'):
            order_numbers_in_feed = order_feed_page.get_order()
            assert last_order_number in order_numbers_in_feed


    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_orders_module_all_time_counter_increases(self, browser, prepare_for_order):
        _, email, password, auth, order_feed_page, _, constructor = prepare_for_order
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            auth.login(email, password)
        with allure.step('Открываем страницу "Лента заказов"'):
            order_feed_page.click_order_feed_button()
        with allure.step('поиск счетчика заказов за все время'):
            order_feed_page.find(completed_all_time)
        with allure.step('Сохраняем кол-во заказов до создания нового'):
            count_number = order_feed_page.get_completed_all_time()
        with allure.step('Собираем бургер и оформляем заказ'):
            constructor.create_order_and_check_in_feed(browser)
        with allure.step('Проверяем, что новое значение не равно "count_number"'):
            assert order_feed_page.get_completed_all_time() != count_number


    @allure.title('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_create_new_order_increases_today_counter(self, browser, prepare_for_order):
        _, email, password, auth, order_feed_page, _, constructor = prepare_for_order
        with allure.step('Открываем страницу c конструктором. Проходим авторизацию'):
            auth.login(email, password)
        with allure.step('Добавляем ожидание для загрузки страницы с конструктором'):
            constructor.wait_for_page_load(f'{URL}')
        with allure.step('Открываем страницу "Лента заказов"'):
            order_feed_page.click_order_feed_button()
        with allure.step('Поиск счетчика заказов за сегодня'):
            order_feed_page.find(completed_all_time)
        with allure.step('Сохраняем кол-во заказов сегодня до создания нового'):
            count_number = order_feed_page.get_completed_today()
            constructor.create_order_and_check_in_feed(browser)
        with allure.step('Проверяем, что новое значение не равно "count_number"'):
            assert order_feed_page.get_completed_today() != count_number

    @allure.title('после оформления заказа его номер появляется в разделе "В работе".')
    def test_new_order_appears_in_work_section(self, browser, prepare_for_order):
        _, email, password, auth, order_feed_page, _, constructor = prepare_for_order
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
            number_order ='0'+ constructor.get_modal_order_text()
        with allure.step('Закрываем окно с заказом'):
            constructor.get_close_modal_order()
        with allure.step('Открываем страницу "Лента заказов"'):
            order_feed_page.click_order_feed_button()
        with allure.step('Получаем номер заказа в работе'):
            count_number = order_feed_page.get_at_work()
        with allure.step('Сравниваем, что номер заказа в работе совпадает с "number_order"'):
            assert count_number == number_order

