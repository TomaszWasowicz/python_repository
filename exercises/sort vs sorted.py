L = (1, 6, 54, 19, 7, 9, 3, 4, 65, 78, 1, 2)  # tuple

# sorted() method sorts the given sequence either in ascending order or in descending order
# and always return the a sorted list. This method doesnot effect the original sequence.

print(L)
print(sorted(L, reverse=False))

# sort() function is very similar to sorted() but unlike sorted it returns nothing
# and makes changes to the original sequence.
# Moreover, sort() is a method of list class and can only be used with lists.

P = ['blue', 'green', 'yellow', 'brown', 'white', 'red']
print(P)
P.sort(reverse=False)
print(P)
