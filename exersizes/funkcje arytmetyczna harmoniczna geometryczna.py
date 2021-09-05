def arithmetic():
    squares = []
    for x in range(20):
        squares.append(x ** 2)
    result = sum(squares)/20.0
    return result

print(arithmetic())

def harmonic(a):
    dividend = 0
    for element in a:
        dividend = (element ** - 1) + dividend
    result = (dividend / len(a)) ** -1
    return result

print(harmonic([1,4,9]))

def geometric(a):
    result = 1
    for element in a:
        result = (element ** (1/len(a))) * result
    return result

print ( geometric([5,7]))







