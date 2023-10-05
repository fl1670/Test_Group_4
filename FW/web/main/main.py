import allure

from FW.web.any_page import AnyPage


class Locator:
    news_tabs_tab_auto = ('xpath', '//*[@data-testid="news-tabs-tab-item-auto"]')


class Main(AnyPage):

    @allure.step('Нажимаем таб новости авто')
    def click_news_tabs_tab_auto(self):
        self.find_element(Locator.news_tabs_tab_auto).click()

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.get_driver().get('https://mail.ru/')
