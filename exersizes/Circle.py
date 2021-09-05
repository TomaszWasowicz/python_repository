import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.perimeter = 0
        self.area = 0

    def calculate_perimeter(self):
        self.perimeter = 2 * self.radius * math.pi
        return self.perimeter

    def calculate_area(self):
        self.area = math.pi * (self.radius ** 2)
        return self.area


if __name__ == "__main__":
    crc1 = Circle(5)
    crc1.calculate_perimeter()
    crc1.calculate_area()
