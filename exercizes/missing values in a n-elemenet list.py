def brakujace_numery(zakres_liczb_w_zbiorze, zbior_liczb):
    return list(set(range(zbior_liczb)) - set(zakres_liczb_w_zbiorze))

print(brakujace_numery([6,8,9], 20))




def missing_value(ns, n):
    return list(set(range(n)) - set(ns))


print(missing_value([1, 3, 4, 5, 6, 7, 8], 10))