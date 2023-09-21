

class FWBase:

    def __init__(self, ApplicationManager):
        self.manager = ApplicationManager

    def get_driver(self):
        if self.manager.driver_instance.driver is None:
            self.manager.driver_instance.start_driver()
        return self.manager.driver_instance.driver
