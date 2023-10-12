import allure
import requests
from FW.api.api_base import ApiBase


class Token(ApiBase):

    @allure.step('Получение токена для пользователя {login}. get_token')
    def post_token(self, login=None, password=None, refresh_token=None):
        url = self.get_base_url() + '/api/Token'

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

    def get_token(self, login=None, password=None, refresh_token=None):

        if login is None:
            login = self.manager.group_data.users['user1']['log']

        if password is None:
            password = self.manager.group_data.users['user1']['pass']

        response = self.post_token(login, password, refresh_token)

        self.manager.group_data.access_token = response['access_token']
        self.manager.group_data.token_type = response['token_type']
        self.manager.group_data.refresh_token = response['refresh_token']
