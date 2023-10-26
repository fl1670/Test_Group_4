from Tests.test_base import TestBase


class PreConditions(TestBase):

    def setup_class(self):
        pass

    def teardown_class(self):
        self.APP.driver_instance.stop_driver()

    def setup_method(self):
        self.APP.any_page.open_main_page()

    def teardown_method(self):
        pass
