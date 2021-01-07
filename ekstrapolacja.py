# Program Tomasza Wąsowicza
# Ekstrapolacja liniowa

def extrapolate(d, x):                                                              # funkcja ekstrapolate
    y = (d[0][1] + (x - d[0][0]) / (d[1][0] - d[0][0]) * (d[1][1] - d[0][1]));      # Wzór na ekstrapolację liniową
    return y;                                                                       # Zwracam wartość y

d = [[14, 8], [15, 6.5]];                                                           # Dane użyte do ekstrapolacji, z godzin 14 oraz 15

x = 14.45;                                                                          # wartosc x - godzina 14.45

print("Wartość y dla x = 14.45 :",extrapolate(d, x));                               #wydrukowanie i wywołanie funkcji extrapolate

