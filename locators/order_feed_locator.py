from selenium.webdriver.common.by import By

order_history = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem') and contains(@class, 'mb-6')]")
popup_order_history = (By.XPATH, "//div[contains(@class, 'Modal_orderBox') and contains(@class, 'Modal_modal__contentBox')]")
order_number = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox') and contains(@class, 'mb-6')]/p[contains(text(), 'Сегодня')]/preceding-sibling::p")
completed_all_time = (By.XPATH, "//p[contains(., 'Выполнено за все время:')]/following-sibling::p[contains(@class, 'OrderFeed_number') and contains(@class, 'text_type_digits-large')]")
completed_today = (By.XPATH, "//p[contains(., 'Выполнено за сегодня:')]/following-sibling::p[contains(@class, 'OrderFeed_number') and contains(@class, 'text_type_digits-large')]")
at_work = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady') and contains(@class, 'OrderFeed_orderList')]/li[contains(@class, 'text') and contains(@class, 'text_type_digits-default') and contains(@class, 'mb-2')]")
order_feed_button = (By.XPATH, "//p[contains(., 'Лента Заказов')]")
number = (By.CSS_SELECTOR,'#root>div>main>div>div>ul')
