def frange(start, stop, step):
    i2 = start
    while i2 < stop:
        yield i2
        i2 += step


for i in frange(2.0, 6.0, 0.5):  # solution 1
    print(i)

print(list(frange(2.0, 6.0, 0.5)))  # solution 2


def numbers(x):
    for i in range(x):
        if i % 3 == 0:
            yield i


print(list(numbers(11)))


def make_word():
    word = ""
    for i in "spam":
        word += i
        yield word


print(list(make_word()))
