import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FWBase:

    def __init__(self, ApplicationManager):
        self.manager = ApplicationManager

    def get_driver(self):
        if self.manager.driver_instance.driver is None:
            self.manager.driver_instance.start_driver()
        return self.manager.driver_instance.driver

    def get_base_url(self):
        return self.manager.group_data.base_url

    @allure.step('request_log')
    def request_logs(self, type='', url='', headers='', body="", status_code='', response_text='', params=''):
        pass

    @allure.step('find_element {locator}')
    def find_element(self, locator, wait=30):
        try:
            web_element = WebDriverWait(self.get_driver(), wait).until(EC.presence_of_element_located(locator))
            return web_element
        except:
            pass

    @allure.step('find_elements {locator}')
    def find_elements(self, locator, wait=30):
        try:
            return WebDriverWait(self.get_driver(), wait).until(EC.presence_of_all_elements_located(locator))
        except:
            pass
