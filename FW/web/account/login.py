import allure

from selenium.webdriver.common.by import By

from FW.web.any_page import AnyPage


class Locator:
    input_login = (By.XPATH, '//input[@id="Input_UserName"]')
    input_password = (By.XPATH, '//input[@id="Input_Password"]')
    local_submit_button = (By.XPATH, '//button[@id="login-submit"]')


class Login(AnyPage):

    @allure.step('Вход по логину и паролю')
    def g1_login_log_pas(self, login=None, password=None):
        if 'Identity' in self.get_current_url():
            if login == None and password == None:
                login = self.manager.group_data.users['user1']['log']
                password = self.manager.group_data.users['user1']['pass']
            self.g1_fill_login(login)
            self.g1_fill_password(password)
            self.g1_click_button_sign_in()
        return self

    @allure.step('Заполнить логин пользователя')
    def g1_fill_login(self, login):
        self.send_keys(Locator.input_login, login)
        return self

    @allure.step('Заполнить пароль пользователя')
    def g1_fill_password(self, password):
        self.send_keys(Locator.input_password, password)
        return self

    @allure.step('Нажать кнопку Вход')
    def g1_click_button_sign_in(self):
        self.click_element(Locator.local_submit_button)
        return self
