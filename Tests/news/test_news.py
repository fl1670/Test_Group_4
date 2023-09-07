from Tests.pre_conditions import PreConditions


class TestNews(PreConditions):

    def setup_class(self):
        print('setup_class')

    def teardown_class(self):
        print('teardown_class')

    def setup_method(self):
        print('setup_method')

    def teardown_method(self):
        print('teardown_method')




    def test_search(self):
        print('test_search')

    def search_2(self):
        print('test_search_2')

    def test_search_3(self):
        print('test_search_3')

    def test_search_4(self):
        print('test_search_4')