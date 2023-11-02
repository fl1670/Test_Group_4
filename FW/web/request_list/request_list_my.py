from FW.web.any_page import AnyPage
from selenium.webdriver.common.by import By


class Locator:
    table_head = (By.XPATH, '//div[@id="grid"]/div[@class="tr-header"]/..')
    table_line = (By.XPATH, '//div[@id="grid"]/div[@data-id]')


class RequestListMy(AnyPage):

    def get_text_table(self):
        elements = self.find_elements(Locator.table_line)
        text = []
        for el in elements:
            text.append(el.text)
        return text
