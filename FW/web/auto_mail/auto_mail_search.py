from FW.web.auto_mail.auto_mail import AutoMail


class AutoMailSearch(AutoMail):

    def get_text_search_result(self):
        frame = self.get_driver().find_element('xpath', '//*[@id="grid"]/div[2]/div/iframe')
        self.get_driver().switch_to.frame(frame)
        elements = self.get_driver().find_elements('xpath', '//ul[@id="search-result"]/li')
        self.get_driver().switch_to.default_content()

        elements_text = []
        for element in elements:
            try:
                elements_text.append(element.text)
            except:
                pass
        print(len(elements_text))
        return elements_text