import time

from FW.web.any_page import AnyPage
from selenium.webdriver.common.by import By


class Locator:
    btn_requests = (By.XPATH, '//div[@data-anchor="Requests"]')
    btn_top_menu_my = (By.XPATH, '//div[@data-anchor="Requests"]/..//div[@data-anchor="TopMenuMy"]')


class Main(AnyPage):

    def click_requests_my(self):
        self.move_to_element(Locator.btn_requests)
        time.sleep(0.5)
        self.click_element(Locator.btn_top_menu_my)



