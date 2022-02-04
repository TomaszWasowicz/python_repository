numbers = [20, 20, 30, 30, 40]


def get_unique_numbers(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique

print(get_unique_numbers(numbers))

