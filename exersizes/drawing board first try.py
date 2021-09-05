# Program gra planszowa
# Napisany przez Tomasza Wąsowicza

"""gra planszowa, narysować plansze, prostokątną, nie znamy rozmiaru
funkcja, ktora narysuje plansze
prostokaty oddzielone znaczkiem *
podaje wspolrzedne"""

x = int(input("podaj parametr x - szerokosz planszy"))
y = int(input("podaj paramter y - wysokość planszy"))


def board_draw(x, y, shape="*"):
    '''funkcja sluzy do rysowania planszy
    '''
    for i in range(y):
        print(shape * (x * 2) + shape)
        print((shape + " ") * x + shape)
    print(shape * (x * 2) + shape)


board_draw(x, y, "?")


