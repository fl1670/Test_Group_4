import time

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('https://mail.ru/')

    driver.find_element('xpath', '//*[@data-testid="news-tabs-tab-item-auto"]').click()

    frame = driver.find_element('xpath', '//*[@id="grid"]/div[2]/div[3]/div/div[1]/div/form/iframe')
    driver.switch_to.frame(frame)
    driver.find_element('xpath', '//input[@name="text"]').send_keys('Новый Hyundai Santa Fe')
    driver.find_element('xpath', '//input[@name="text"]').send_keys(Keys.ENTER)
    driver.switch_to.default_content()
    time.sleep(2)
    
    frame = driver.find_element('xpath', '//*[@id="grid"]/div[2]/div/iframe')
    driver.switch_to.frame(frame)
    elements = driver.find_elements('xpath', '//ul[@id="search-result"]/li')

    elements_text = []
    for element in elements:
        elements_text.append(element.text)

    result = []
    for text in elements_text:
        if 'Hyundai Santa Fe' in text:
            result.append(True)
        else:
            result.append(False)

    assert any(result)

    driver.switch_to.default_content()
    driver.quit()





