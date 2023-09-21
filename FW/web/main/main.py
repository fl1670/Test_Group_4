from FW.web.any_page import AnyPage


class Main(AnyPage):

    def click_news_tabs_tab_auto(self):
        self.get_driver().find_element('xpath', '//*[@data-testid="news-tabs-tab-item-auto"]').click()

    def open_main_page(self):
        self.get_driver().get('https://mail.ru/')
