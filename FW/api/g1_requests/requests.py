import allure

from FW.api.api_base import ApiBase


class Requests(ApiBase):

    @allure.step('Заявки в системе с учетом фильтра, сортировки с постраничным выводом')
    def get_requests(self, params=None):
        return self.requests_GET(self.get_base_url() + '/Requests', params=params)

    @allure.step('Создание новой заявки')
    def post_requests(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/Requests', body, params=params)

    @allure.step('Заявка с номером Id ({id})')
    def get_requests_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/Requests/{id}', params=params)

    @allure.step('Удаляет вложенную заявку с номером SubRequestId из заявки с номером Id')
    def delete_requests_id_sub_requests_id(self, id, sub_request_id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/Requests/{id}/SubRequests/{sub_request_id}', params=params)
