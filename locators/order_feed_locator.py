from selenium.webdriver.common.by import By

order_history = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']")
popup_order_history = (By.XPATH, "//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']")
order_number = (By.XPATH, "//div[@class='OrderHistory_textBox__3lgbs mb-6']/p[contains(text(), 'Сегодня')]/preceding-sibling::p")
completed_all_time = (By.XPATH, "//p[contains(., 'Выполнено за все время:')]/following-sibling::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
completed_today = (By.XPATH, "//p[contains(., 'Выполнено за сегодня:')]/following-sibling::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
at_work = (By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")
order_feed_button = (By.XPATH, "//p[contains(., 'Лента Заказов')]")
number = (By.CSS_SELECTOR,'#root>div>main>div>div>ul')