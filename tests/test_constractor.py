import allure
from data import DEFAULT_ORDER_NUMBER, INGREDIENT_DETAILS, COUNT_INGREDIENT
from url import LOGIN, URL, FEED


class TestToConstructor:

    @allure.title('переход по клику на «Лента заказов»')
    def test_navigate_to_order_feed(self, browser, prepare_for_constructor):
        response, _, _, _, constructor, order_feed_page = prepare_for_constructor
        with allure.step('Открываем страницу авторизации'):
            constructor.open(f'{URL}{LOGIN}')
        with allure.step('Нажимаем кнопку "Лента заказов"'):
            order_feed_page.click_order_feed_button()
        with allure.step('Проверяем переход на страницу "Лента заказов"'):
            assert constructor.get_current_url() == f'{URL}{FEED}'


    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient_displays_popup_with_details(self, browser, prepare_for_constructor):
        _, _, _, _, constructor, _ = prepare_for_constructor
        with allure.step('Открываем страницу с конструктором'):
            constructor.open()
        with allure.step('Нажимаем на ингредиент'):
            constructor.click_ingredient()
        with allure.step('Проверяем, что появилось модальное окно и содержит текст "INGREDIENT_DETAILS"'):
            assert constructor.get_modal_window_ingredient() == INGREDIENT_DETAILS

    @allure.title('всплывающее окно закрывается кликом по крестику')
    def test_ingredient_popup_close(self, browser, prepare_for_constructor):
        _, _, _, _, constructor, _ = prepare_for_constructor
        with allure.step('Открываем страницу с конструктором'):
            constructor.open()
        with allure.step('Нажимаем на ингредиент'):
            constructor.click_ingredient()
        with allure.step('Закрываем окно с ингредиентом'):
            constructor.click_close_modal_window_ingredient()
        with allure.step('Проверяем, что окно больше не отображается'):
            assert 'Modal_modal__P3_V5' in constructor.get_modal_class()

    @allure.step('при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_counter_increments_when_ingredient_added_to_order(self, browser, prepare_for_constructor):
        _, _, _, _, constructor, _ = prepare_for_constructor
        with allure.step('Открываем страницу с конструктором'):
            constructor.open()
        with allure.step('Получаем ингредиент и конструктор бургера'):
            ingredient = constructor.get_ingredient()
            burger_constructor = constructor.get_constructor_burger()
        with allure.step('Перетаскиваем ингредиент в конструктор'):
            constructor.drag_and_drop_element(ingredient, burger_constructor)
        with allure.step('Проверяем, что счетчик ингредиента увеличился'):
            assert constructor.get_count_ingredient() == COUNT_INGREDIENT

    @allure.step('залогиненный пользователь может оформить заказ.')
    def test_user_can_place_order(self, browser, prepare_for_constructor):
        _, email, password, auth, constructor, _ = prepare_for_constructor
        with allure.step('Открываем страницу с конструктором. Проходим авторизацию'):
            auth.login(email, password)
        with allure.step('Добавляем ожидание для загрузки страницы с конструктором'):
            constructor.wait_for_page_load(f'{URL}')
        with allure.step('Собираем бургер и оформляем заказ'):
            constructor.create_burger_and_place_order()
        with allure.step('Добавляем ожидание'):
            constructor.wait_loading_visibility(browser)
            constructor.wait_loading_invisibility(browser)
        with allure.step('Проверяем, что номер заказа не равно 9999'):
             assert constructor.get_modal_order_text() != DEFAULT_ORDER_NUMBER