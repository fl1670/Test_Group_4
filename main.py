def summ(a):
    summ = ''
    for value in a:
        summ = summ + value
    return summ


def min_asd(a, b):
    if a < b:
        return a
    else:
        return b


def print_pet_names(owner, test=123,  **pets):
    print(f"Owner Name: {owner}")
    for pet, name in pets.items():
        print(f"{pet}: {name}")
    return owner, 321, {'test': 12312}


def bread(func):
    def wrapper():
        print()
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")
    return wrapper

def box(func):
    def wrapper():
        func()
        print('=========================')
    return wrapper


@box
@bread
@ingredients
def sandwich(food="--ветчина--"):
    print(food)


if __name__ == '__main__':
    sandwich()

    # sandwich = bread(ingredients(sandwich))
    # sandwich()

    # temp = print_pet_names("Jonathan", dog="Brock", fish=["Larry", "Curly", "Moe"], turtle="Shelldon")
    # print(temp)

