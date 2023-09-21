from FW.web.auto_mail.auto_mail import AutoMail
from FW.web.auto_mail.auto_mail_search import AutoMailSearch
from FW.web.driver_Instance import DriverInstance
from FW.web.main.main import Main


class ApplicationManager:

    def __init__(self):
        self.driver_instance = DriverInstance()

        self.web_main = Main(self)
        self.web_auto_mail = AutoMail(self)
        self.web_auto_mail_search = AutoMailSearch(self)
