from Data.group_data import GroupData
from FW.api.g1_requests.requests import Requests
from FW.api.token import Token
from FW.web.auto_mail.auto_mail import AutoMail
from FW.web.auto_mail.auto_mail_search import AutoMailSearch
from FW.web.driver_Instance import DriverInstance
from FW.web.main.main import Main


class ApplicationManager:
    group_data = GroupData

    def __init__(self):
        self.driver_instance = DriverInstance()

        self.web_main = Main(self)
        self.web_auto_mail = AutoMail(self)
        self.web_auto_mail_search = AutoMailSearch(self)
        self.api_token = Token(self)
        self.api_requests = Requests(self)
