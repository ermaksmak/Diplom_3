from selenium.webdriver.common.by import By

button_personal_account = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
order_history_link = (By.XPATH, "//a[@href='/account/order-history']")
button_exit = (By.XPATH, "//button[@type='button' and contains(@class, 'Account_button') and contains(@class, 'text_color_inactive') and text()='Выход']")
title_authorizations = (By.XPATH, "//h2[text()='Вход]")
order_history_item = (By.XPATH,"//div[contains(@class, 'OrderHistory_orderHistory')]/ul/li/a/div[contains(@class, 'OrderHistory_textBox')]/p[contains(@class, 'text') and contains(@class, 'text_type_digits-default')]")
