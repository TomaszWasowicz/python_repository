#immutable - NIEMUTOWALNE, NIEZMIENIALNE

# Creating a Set
people = {"Jay", "Idrish", "Archi"}
print("People:", end=" ")
print(people)

people.add("Daxit")

for i in range(1, 6):
    people.add(i)

print("\nSet after adding element:", end=" ")
print(people)


