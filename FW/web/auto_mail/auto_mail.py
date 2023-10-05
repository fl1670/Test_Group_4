import allure

from FW.web.any_page import AnyPage
import time

from selenium.webdriver.common.keys import Keys


class Locator:
    input_text_in_search = ('xpath', '//input[@name="text"]')
    iframe_input_text_in_search = ('xpath', '//*[@id="grid"]/div[2]/div[3]/div/div[1]/div/form/iframe')


class AutoMail(AnyPage):

    @allure.step('Вводим текст в строку поиска')
    def input_text_in_search(self, text):
        frame = self.find_element(Locator.iframe_input_text_in_search)
        self.get_driver().switch_to.frame(frame)

        self.find_element(Locator.input_text_in_search).send_keys(text)
        self.find_element(Locator.input_text_in_search).send_keys(Keys.ENTER)

        self.get_driver().switch_to.default_content()
