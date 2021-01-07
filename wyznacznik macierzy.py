import numpy as np                              #importuję moduł numpy

X = 10                                           #pierwszy rozmiar tablicy
Y = 10                                           #drugi rozmiar tablicy

tablica = np.array(np.random.random((X, Y)))     #tworzę za pomocą modułu numpy losową tablicę o wskazanych parametrach

wskaznik = np.linalg.det(tablica)                #za pomocą instrukcji linalg.det liczę wskaźnik tablicy

print(wskaznik)                                  #wyświetlam rezultat