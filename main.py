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


if __name__ == '__main__':
    temp = print_pet_names("Jonathan", dog="Brock", fish=["Larry", "Curly", "Moe"], turtle="Shelldon")
    print(temp)
