# Program Tomasza Wąsowicza
# Interpolacja wielomianowa formuła Langrange's

class Data:                                                                             #tworzę klasę Data
    def __init__(self, x, y):                                                           #metoda wywołująca się, o parametrach x i y
        self.x = x
        self.y = y

def interpolate(f: list, xi: float, n: float) -> float:                                 #funkcja "interpolate", która posiada parametry f: lista, xi: zmienna typu float ( która przedstawia nowy punkt x, ktory chce uzyskac ) i n( liczba zestawów danych, punktów danych ) typu float

    result = 0.0                                                                        # Inicjalizacja "result"
    for i in range(n):                                                                  #pętla for dla parametru i o zasięgu n

        term = f[i].y                                                                   #"term" to indywidualny wynik funkcji f(i) parametru y
        for j in range(n):                                                              #pętla for dla parametru j o zasięgu n
            if j != i:                                                                  # jeśli parametr j jest różny od parametru j
                term = term * (xi - f[j].x) / (f[i].x - f[j].x)                         # wywołaj formułę Lagrange'a, której rezultatem jest

        result += term                                                                  # do rezultatu dodaję wynik formuły "term" za pomocą wyrażenia "+="

    return result                                                                       # zwracam rezultat funkcji

if __name__ == "__main__":                                                                  # pętla if dla zestawu danych

    f = [Data(1, 0.10), Data(2, 0.11), Data(3, 0.90), Data(4, 0.12), Data(5, 0.42),         # tablica z 24 znanymi zestawami danych, w tym jeden zestaw pusty
         Data(6, 0.10), Data(7, 1.02), Data(8, 4), Data(9, 5.27), Data(10, 4.09),
         Data(11, 8), Data(12, 8), Data(13, 3.20), Data(14, 8), Data(0,0), Data(15, 6.50),
         Data(16, 1.20), Data(17, 1.90), Data(18, 0.90), Data(19, 1.10), Data(20, 0.25),
         Data(21, 0.20), Data(22, 0.19), Data(23, 0.20)]

    print("Wartość f(14.45) jest równa :", interpolate(f, 14.45, 24))                              #wydrukowanie i wywoływanie funkcji "interpolate" , by uzyskać szukane wartości y, dla x równego x = 15.30

    print("Wartość f(15.30) jest równa :", interpolate(f, 15.30, 24))                              #wydrukowanie i wywoływanie funkcji "interpolate" , by uzyskać szukane wartości y, dla x równego x = 14.45

    print("Wartość f(10.30) jest równa :", interpolate(f, 10.30, 24))

    print("Wartość f(12.30) jest równa :", interpolate(f, 12.30, 24))
