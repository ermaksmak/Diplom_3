from selenium.webdriver.common.by import By

constructor_button = (By.XPATH, "//p[contains(., 'Конструктор')]")
ingredient = (By.XPATH, "*//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")
buns = (By.XPATH, "//p[contains(., 'Флюоресцентная булка R2-D3')]")
arrange_order_button = (By.XPATH, "//button[contains(., 'Оформить заказ')]")
modal_window_ingredient = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_modified") and contains(@class, "Modal_modal__title")]')
close_modal_window_ingredient = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]/*/button[contains(@class, 'Modal_modal__close_modified') and contains(@class, 'Modal_modal__close')]")
close_modal = (By.XPATH, "//div[contains(@class,'App_App')]/section[contains(@class,'Modal_modal')]")
constructor_burger = (By.XPATH, '//ul[contains(@class, "BurgerConstructor_basket__list__")]')
count_ingredient = (By.XPATH, "//p[@class='counter_counter__num__3nue1'][contains(., '2')]")
modal_order = (By.XPATH, '//h2[contains(@class, "Modal_modal__title__") and contains(@class, "text_type_digits-large")]')
close_modal_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/*/button[contains(@class, "Modal_modal__close_modified__3V5XS")]')
LOADING = (By.XPATH,'//img[contains(@class, "Modal_modal__loading")]')
number = (By.CSS_SELECTOR,'#root>div>main>div>div>ul')



