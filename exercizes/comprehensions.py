# 1. Lists

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

# 2. dictionaries

mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys()}
print(mcase_frequency)
# {v: k for k, v in some_dict.items()}

# 3. sets

squared = {x ** 2 for x in [1, 1, 2]}
print(squared)

# 4. generators

multiples_gen = (i for i in range(30) if i % 3 == 0)
#print(multiples_gen)
# Output: <generator object <genexpr> at 0x7fdaa8e407d8>
for x in multiples_gen:
    print(x)
