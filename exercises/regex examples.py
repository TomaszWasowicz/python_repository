import re

txt = "My time is right, I am right on time, it is my time."

x = re.split("\s", txt, 1)  # oddziel od stringa tylko 1 wyraz
y = re.findall("time", txt)

print(x)
print(y)

z = re.search("My time is", txt)  # search

print(z)

g = re.sub("t", "r", txt)  # substitution

print(g)

u = "Always look on the bright side of life"

splitting_u = re.split('', u)
print(splitting_u)

splitting_u.remove('')  # removing splitting sign, here an empty space
print(splitting_u)

