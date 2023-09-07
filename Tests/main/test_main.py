import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Tests.pre_conditions import PreConditions


class TestMain(PreConditions):
    driver = None

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_class(self):
        self.driver.quit()

    def setup_method(self):
        self.driver.get('https://mail.ru/')

    def teardown_method(self):
        pass

    def test_search(self):
        self.driver.find_element('xpath', '//*[@data-testid="news-tabs-tab-item-auto"]').click()

        frame = self.driver.find_element('xpath', '//*[@id="grid"]/div[2]/div[3]/div/div[1]/div/form/iframe')
        self.driver.switch_to.frame(frame)
        self.driver.find_element('xpath', '//input[@name="text"]').send_keys('Новый Hyundai Santa Fe')
        self.driver.find_element('xpath', '//input[@name="text"]').send_keys(Keys.ENTER)
        self.driver.switch_to.default_content()
        time.sleep(4)

        frame = self.driver.find_element('xpath', '//*[@id="grid"]/div[2]/div/iframe')
        self.driver.switch_to.frame(frame)
        elements = self.driver.find_elements('xpath', '//ul[@id="search-result"]/li')
        self.driver.switch_to.default_content()

        elements_text = []
        for element in elements:
            try:
                elements_text.append(element.text)
            except:
                pass
        print(len(elements_text))

        result = []
        for text in elements_text:
            if 'Hyundai Santa Fe' in text:
                result.append(True)
            else:
                result.append(False)

        assert any(result)

    def test_search_2(self):
        self.driver.find_element('xpath', '//*[@data-testid="news-tabs-tab-item-auto"]').click()

        frame = self.driver.find_element('xpath', '//*[@id="grid"]/div[2]/div[3]/div/div[1]/div/form/iframe')
        self.driver.switch_to.frame(frame)
        self.driver.find_element('xpath', '//input[@name="text"]').send_keys('iPhone 15')
        self.driver.find_element('xpath', '//input[@name="text"]').send_keys(Keys.ENTER)
        self.driver.switch_to.default_content()
        time.sleep(4)

        frame = self.driver.find_element('xpath', '//*[@id="grid"]/div[2]/div/iframe')
        self.driver.switch_to.frame(frame)
        elements = self.driver.find_elements('xpath', '//ul[@id="search-result"]/li')
        self.driver.switch_to.default_content()

        elements_text = []
        for element in elements:
            try:
                elements_text.append(element.text)
            except:
                pass
        print(len(elements_text))

        result = []
        for text in elements_text:
            if 'iPhone 15' in text:
                result.append(True)
            else:
                result.append(False)

        assert any(result)



