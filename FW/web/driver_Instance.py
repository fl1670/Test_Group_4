from selenium import webdriver


class DriverInstance:

    driver = None

    def start_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        return self.driver

    def stop_driver(self):
        self.driver.quit()
