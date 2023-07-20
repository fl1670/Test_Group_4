from sandwich.sandwich import Sandwich


class Sandwich2(Sandwich):

    def box(self):
        temp = self.req.get('https://yandex.ru/')
        print('-------------------------')
        print('-------------------------')
        return temp

    def add_ingredients(self):
        print("~хлеб~")
        print("~колбаса~")
