from selenium.webdriver.common.by import By

email_input = (By.XPATH, "//input[contains(@class, 'text') and contains(@class, 'input__textfield') and contains(@class, 'text_type_main-default') and @type='text' and @name='name']")
password_input = (By.XPATH, "//input[contains(@class, 'text') and contains(@class, 'input__textfield') and contains(@class, 'text_type_main-default') and @type='password' and @name='Пароль']")
button_enter = (By.XPATH, "//button[contains(@class, 'button_button') and contains(@class, 'button_button_type_primary') and contains(@class, 'button_button_size_medium') and text()='Войти']")