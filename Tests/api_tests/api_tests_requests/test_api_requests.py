from Tests.test_base import TestBase


class TestApiRequests(TestBase):

    def test_requests_1(self):
        request = self.APP.api_requests.get_requests_id(1524420)

        assert 'API Test request 11.10.2023 15:08' == request['Description']
        assert len(request['Approvers']) > 2
