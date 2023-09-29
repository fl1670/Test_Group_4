import allure

from Tests.api_tests.api_pre_conditions import ApiPreConditions


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка получения Токена')
class TestToken(ApiPreConditions):

    @allure.title('Тест получения токена')
    def test_get_token(self):
        login = self.APP.group_data.users['user1']['log']
        password = self.APP.group_data.users['user1']['pass']

        response = self.APP.api_token.post_token(login=login, password=password)
        assert 'access_token' in response
        assert 'token_type' in response
        assert 'refresh_token' in response

    @allure.title('Тест получения токена через refresh_token')
    def test_get_token_refresh_token(self):
        login = self.APP.group_data.users['user1']['log']
        password = self.APP.group_data.users['user1']['pass']
        response = self.APP.api_token.post_token(login, password)

        refresh_token_response = self.APP.api_token.post_token(refresh_token=response['refresh_token'])
        assert 'access_token' in refresh_token_response
        assert 'token_type' in refresh_token_response
        assert 'refresh_token' in refresh_token_response
