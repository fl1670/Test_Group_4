from FW.web.any_page import AnyPage
import time

from selenium.webdriver.common.keys import Keys


class AutoMail(AnyPage):

    def input_text_in_search(self, text):
        frame = self.get_driver().find_element('xpath', '//*[@id="grid"]/div[2]/div[3]/div/div[1]/div/form/iframe')
        self.get_driver().switch_to.frame(frame)
        self.get_driver().find_element('xpath', '//input[@name="text"]').send_keys(text)
        self.get_driver().find_element('xpath', '//input[@name="text"]').send_keys(Keys.ENTER)
        self.get_driver().switch_to.default_content()
        time.sleep(4)
