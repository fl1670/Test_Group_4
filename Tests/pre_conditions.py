from Tests.test_base import TestBase


class PreConditions(TestBase):

    driver = None

    def setup_class(self):
        self.APP.driver_instance.start_driver()

    def teardown_class(self):
        self.APP.driver_instance.stop_driver()

    def setup_method(self):
        self.APP.web_main.open_main_page()

    def teardown_method(self):
        pass
