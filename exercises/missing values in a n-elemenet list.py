def missing_values(elements, container):
    return list(set(range(container)) - set(elements))


print(missing_values([1, 2, 4, 6, 7, 9, 20], 40))


def brakujące_wartości(elementy, pojemnik):
    return list(set(range(pojemnik)) - set(elementy))


print(brakujące_wartości([2, 8, 5, 9, 1, 16], 20))
