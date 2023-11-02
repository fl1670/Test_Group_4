import allure

from Tests.pre_conditions import PreConditions


@allure.epic('G1')
@allure.feature('Web')
@allure.story('Проверка главной страницы')
class TestMain(PreConditions):

    def test_first_test(self):
        self.APP.main.click_requests_my()
        text = self.APP.request_list_my.get_text_table()

        for element in text:
            if 'Automation' in element:
                print('PASS\n')
