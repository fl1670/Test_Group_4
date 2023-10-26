from Data.group_data import GroupData
from FW.api.g1_requests.requests import Requests
from FW.api.token import Token
from FW.web.account.login import Login
from FW.web.any_page import AnyPage
from FW.web.driver_Instance import DriverInstance
from FW.work_with_time import WorkWithTime


class ApplicationManager:
    group_data = GroupData

    def __init__(self):
        self.driver_instance = DriverInstance()

        self.any_page = AnyPage(self)
        self.api_token = Token(self)
        self.api_requests = Requests(self)
        self.time = WorkWithTime()
        self.login = Login(self)
