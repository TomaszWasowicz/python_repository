def missing_values(range_of, container):
    return list(set(range(container)) - set(range_of))


print(missing_values([1, 2, 4, 6, 7, 9, 20], 40))


