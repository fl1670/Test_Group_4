import allure
import requests
from FW.api.api_base import ApiBase


class Token(ApiBase):

    @allure.step('Получение токена для пользователя {login}. get_token')
    def post_token(self, login=None, password=None, refresh_token=None):
        url = 'https://api-test-compose.gandiva.ru/api/Token'

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            'grant_type': 'password',
            'username': login,
            'password': password
        }

        if refresh_token is not None:
            body = {
                'grant_type': 'refresh_token',
                'refresh_token': refresh_token
            }

        response = requests.post(url, data=body, headers=headers)

        return response.json()









