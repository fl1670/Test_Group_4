import allure

from Tests.pre_conditions import PreConditions


@allure.epic('G1')
@allure.feature('Web')
@allure.story('Проверка главной страницы')
class TestMain(PreConditions):

   def test_first_test(self):
       self.APP.login.g1_login_log_pas()

