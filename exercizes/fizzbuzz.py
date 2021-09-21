from unicodedata import decimal

n = int(input("input an integer: "))

for i in range(1, n, 3):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "fizzbuzz")
        continue
    elif i % 3 == 0:
        print(i, "fizz")
        continue
    elif i % 5 == 0:
        print(i, "buzz")
        continue
    print(i)