from FW.FW_base import FWBase

import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class WebBase(FWBase):

    def get_driver(self):
        if self.manager.driver_instance.driver is None:
            self.manager.driver_instance.start_driver()
        return self.manager.driver_instance.driver

    def get_base_url(self):
        return self.manager.group_data.base_url

    def get_current_url(self):
        return self.get_driver().current_url

    @allure.step('click')
    def click_element(self, locator):
        web_element = self.find_element(locator)
        web_element.click()

    @allure.step('Send keys')
    def send_keys(self, locator, text):
        web_element = self.find_element(locator)
        web_element.send_keys(text)

    def scroll_to_element(self, locator):
        element = self.find_element(locator).location_once_scrolled_into_view
        script = "window.scrollBy(" + str(element['x'] - 180) + ", " + str(element['y'] - 180) + ")"
        self.get_driver().execute_script(script)

    @allure.step("move_to_element")
    def move_to_element(self, locator):
        actions = ActionChains(self.get_driver())
        element = self.find_element(locator)
        actions.move_to_element(element)
        actions.perform()


    @allure.step('find_element {locator}')
    def find_element(self, locator, wait=30):
        try:
            return WebDriverWait(self.get_driver(), wait).until(EC.presence_of_element_located(locator))
        except:
            pass

    @allure.step('find_elements {locator}')
    def find_elements(self, locator, wait=30):
        try:
            return WebDriverWait(self.get_driver(), wait).until(EC.presence_of_all_elements_located(locator))
        except:
            pass
