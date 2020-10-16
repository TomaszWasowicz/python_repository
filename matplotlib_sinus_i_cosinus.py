import matplotlib.pyplot as plt
import math

#Zadanie: sinus i cosinus ( przedzial od 01 do 10)

x = []
y = []
z = []

for i in range(1000):
    j = i/50
    x.append(j)
    y.append(math.sin(j))
    z.append(math.cos(j))

plt.plot(x, y, 'r-')
plt.plot(x, z, 'b-')

plt.show()




