from unicodedata import decimal
import numpy as np
import matplotlib.pyplot as plt

vegetables = ['squash', 'pea', 'carrot', 'potato']
new_list = sorted(vegetables)
print(new_list) # new_list = ['carrot', 'pea', 'potato', 'squash']

print(vegetables) # vegetables = ['squash', 'pea', 'carrot', 'potato']

vegetables.sort()
print(vegetables) # vegetables = ['carrot', 'pea', 'potato', 'squash']



x = [2, 4, 6, 8, 10, 12]
y = [2, 2, 2, 2, 2, 2]

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Constant Complexity')
plt.show()


x = [2, 4, 6, 8, 10, 12]
y = [2, 4, 6, 8, 10, 12]

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Linear Complexity')
plt.show()



x = 10
y = x+1



list_arranged = np.arange(2, 6, 0.5).tolist()
print(list_arranged)

def frange(start, stop, step=0.5):
    i = start
    while i < stop:
        yield i
        i += step

for i in frange(2.0, 6.0, 0.5):     # solution 1
    print(i)

print(list(frange(2.0, 6.0, 0.5)))  #solution 2


new_str = "Abcd efgh ijk lmn opq rstu v w xyz"
print(new_str)
print(new_str[::-1])





Dictionary1 = {'A': 'Geeks','D': 'Geeks', 'B': 'For', 'C': 'Geeks'} #tylko unikalne elementy
Dictionary1[1] = 4 #dodanie klucza 1 i wartosc 4 do niego
print(Dictionary1)
print(Dictionary1.keys()) # Printing keys of dictionary
empty_Dict1 = {} # Creating empty Dictionary
print(empty_Dict1.keys()) # Printing keys of Empty Dictionary
print(Dictionary1.copy())
print(Dictionary1.values())

list = [ 1,1,2,4,8,31,3,6,7,1,5,88,6,9]
print(set(list))

set = {5,67,8,5,43,3,4,4,66,6,7,4,}
print(set)

