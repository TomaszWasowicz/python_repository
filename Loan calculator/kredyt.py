wkz = (int(input("Podaj kwote wnioskowanego kredytu: ")))
irz = (int(input("Podaj ilosc rat: ")))
zma = (int(input("Podaj kwote swoich zarobków: ")))
wap = (int(input("Podaj swój wiek: ")))
rkw = (int(input("Podaj wysokość raty jaką chcesz płacić: ")))

wkb = 500000
print("Wielkosc kredytu jaki może udzielić bank to:", wkb)
irb = 40
print("Ilosc rat kredytu, którego może udzielić bank to:", irb)
rkm = 5000
print("Maksymalna wysokość raty kredytu, którego może udzielić bank to:", irb)
wpm = 60
print("Maksymalny wiek aplikanta to:", irb)


def k(self):
    if wkz <= wkb:
        return 1
    else:
        return 0


def p():
    if irz <= irb:
        return 1
    else:
        return 0


def j():
    if rkw <= (0.2 * rkm):
        return 1
    else:
        return 0


def i():
    if wap <= wpm:
        return 1
    else:
        return 0


wk = k * p * j * i
print(wk)
