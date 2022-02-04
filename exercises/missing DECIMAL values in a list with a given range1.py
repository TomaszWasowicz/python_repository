from decimal import Decimal


def missing_decimals():
    return [Decimal(20 + x * 5) / 10 for x in range(8)]


print(missing_decimals())
