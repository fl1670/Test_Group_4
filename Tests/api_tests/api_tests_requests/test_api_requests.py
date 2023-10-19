import allure

from Tests.test_base import TestBase
import pytest


@allure.feature('Api')
@allure.story('Request')
class TestApiRequests(TestBase):
    testdata = (
        ('user2', 'text', 'testuser02'),
        ('user1', '123123', 'testuser01'),
        ('user3', '', 'testuser03'),
    )

    @allure.title('Получение заявки по Id')
    def test_requests_1(self):
        request = self.APP.api_requests.get_requests_id(1524420)

        assert 'API Test request 11.10.2023 15:08' == request['Description']
        assert len(request['Approvers']) > 2

    @allure.title('Создание заявки')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('description description description')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("user,text,expected", testdata)
    def test_requests_2(self, user, text, expected):

        login = self.APP.group_data.users[user]['log']
        password = self.APP.group_data.users[user]['pass']

        description = f"API Test request {self.APP.time.get_date_time_for_sql_increased_x_days()} -- {text}"

        self.APP.api_token.get_token(login, password)

        body = {
            "department": {"id": 3},
            "category": {"id": 6},
            "requestType": {"id": 6},
            "jobType": {"id": 3906},
            "description": description,
        }
        response = self.APP.api_requests.post_requests(body)

        assert response['Status'] == 6
        assert response['Description'] == description
        assert response['Initiator']['Login'] == expected
