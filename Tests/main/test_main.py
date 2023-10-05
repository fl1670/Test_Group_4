import allure

from Tests.pre_conditions import PreConditions


@allure.epic('G1')
@allure.feature('Web')
@allure.story('Проверка главной страницы')
class TestMain(PreConditions):

    def test_temp(self):
        print(self.APP.group_data.users)

    @allure.title('Проверка поиска "Hyundai Santa Fe"')
    def test_search(self):
        self.APP.web_main.click_news_tabs_tab_auto()
        self.APP.web_auto_mail.input_text_in_search('Новый Hyundai Santa Fe')
        elements_text = self.APP.web_auto_mail_search.get_text_search_result()

        result = []
        for text in elements_text:
            if 'Hyundai Santa Fe' in text:
                result.append(True)
            else:
                result.append(False)

        assert any(result)

    def test_search_2(self):
        self.APP.web_main.click_news_tabs_tab_auto()
        self.APP.web_auto_mail.input_text_in_search('iPhone 15')
        elements_text = self.APP.web_auto_mail_search.get_text_search_result()

        result = []
        for text in elements_text:
            if 'iPhone 15' in text:
                result.append(True)
            else:
                result.append(False)

        assert any(result)



