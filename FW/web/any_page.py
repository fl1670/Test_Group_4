import allure

from FW.web.web_base import WebBase


class AnyPage(WebBase):

    def open_main_page(self):
        self.get_driver().get(self.manager.group_data.base_url_web)

