import math

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.perimeter = 0
        self.area = 0

    def calculate_perimeter(self):
        self.perimeter = 3* self.base
        return self.perimeter

    def calculate_area(self):
        self.area = 0.5 * self.base * self.height
        return self.area


trg1 = Triangle(6, 4)
trg1.calculate_perimeter()
trg1.calculate_area()
