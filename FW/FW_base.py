import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FWBase:

    def __init__(self, ApplicationManager):
        self.manager = ApplicationManager

    @allure.step('request_log')
    def request_logs(self, type='', url='', headers='', body="", status_code='', response_text='', params=''):
        pass
