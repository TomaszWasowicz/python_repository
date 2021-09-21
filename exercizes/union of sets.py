#mutable, iterable, unique elements

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}

population = people.union(vampires)

print("Union using union() function")
print(population)

population = people | dracula

print("\nUnion using '|' operator")
print(population)