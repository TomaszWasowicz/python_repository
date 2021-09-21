import re

txt = "My time is right, I am right on time, it is my time."

x = re.split("\s", txt, 1) # oddziel od stringa tylko 1 wyraz
y = re.findall("time", txt)


print(x)
print(y)


