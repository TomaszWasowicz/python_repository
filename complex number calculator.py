class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def create_number(self):
        self.real = (float(input("Enter a real part of the complex number")))
        self.imaginary = (float(input("Enter an imaginary part of the complex number")))
        return Complex(self.real, self.imaginary)

    def display_number(self):
        print(f"Your complex number is: {Complex(self.real, self.imaginary)}")

    def erase_number(self):
        (self.real, self.imaginary) = (0, 0)
        print(f"Number is erased: {Complex(self.real, self.imaginary)}")

    def __str__(self):
        if type(self.real) == int and type(self.imaginary) == int:
            if self.imaginary >= 0:
                return '%d+%di' % (self.real, self.imaginary)
            elif self.imaginary < 0:
                return '%d%di' % (self.real, self.imaginary)
        else:
            if self.imaginary >= 0:
                return '%f+%fi' % (self.real, self.imaginary)
            elif self.imaginary < 0:
                return '%f%fi' % (self.real, self.imaginary)


class Calculation(object):
    def __init__(self, complex_number):
        self.complex_number = complex_number

    def __add__(self, other):
        result_real = self.complex_number.real + other.complex_number.real
        result_imaginary = self.complex_number.imaginary + other.complex_number.imaginary
        result = Complex(result_real, result_imaginary)
        return result

    def __sub__(self, other):
        result_real = self.complex_number.real - other.complex_number.real
        result_imaginary = self.complex_number.imaginary - other.complex_number.imaginary
        result = Complex(result_real, result_imaginary)
        return result

    def __mul__(self, other):
        result_real = (
                    self.complex_number.real * other.complex_number.real - self.complex_number.imaginary * other.complex_number.imaginary)
        result_imaginary = (
                    self.complex_number.real * other.complex_number.imaginary + other.complex_number.real * self.complex_number.imaginary)
        result = Complex(result_real, result_imaginary)
        return result

    def __truediv__(self, other):
        result_real = float(float(
            self.complex_number.real * other.complex_number.real + self.complex_number.imaginary * other.complex_number.imaginary) / float(
            other.complex_number.real * other.complex_number.real + other.complex_number.imaginary * other.complex_number.imaginary))
        result_imaginary = float(float(
            other.complex_number.real * self.complex_number.imaginary - self.complex_number.real * other.complex_number.imaginary) / float(
            other.complex_number.real * other.complex_number.real + other.complex_number.imaginary * other.complex_number.imaginary))
        result = Complex(result_real, result_imaginary)
        return result

    @staticmethod
    def display_result(result):
        print("The result of the operation is: ", result)


cn1 = Complex(0, 0)
cn2 = Complex(0, 0)
cn3 = Complex(0, 0)

calc1 = Calculation(cn1)
calc2 = Calculation(cn2)
calc3 = Calculation(cn3)


def menu():
    choice = 1
    while choice != 0:
        print("0. Exit")
        print("1. Construction of a complex number 1")
        print("2. Construction of a complex number 2")
        print("3. Display complex number 1")
        print("4. Display complex number 2")
        print("5. Erase complex number 1")
        print("6. Erase complex number 2")
        print("7. Addition")
        print("8. Subtraction")
        print("9. Multiplication")
        print("10. Division")
        print("11. Display the result of calculation")
        choice = int(input("Enter choice: "))

        if choice == 1:
            print("Result: ", cn1.create_number())
        elif choice == 2:
            print("Result: ", cn2.create_number())
        elif choice == 3:
            print("Result: ", cn1.display_number())
        elif choice == 4:
            print("Result: ", cn2.display_number())
        elif choice == 5:
            print("Result: ", cn1.erase_number())
        elif choice == 6:
            print("Result: ", cn2.erase_number())
        elif choice == 7:
            print("Result: ", calc1.__add__(calc2))  # zamiennie moze to byc poprostu c1 + c2
        elif choice == 8:
            print("Result: ", calc1.__sub__(calc2))
        elif choice == 9:
            print("Result: ", calc1.__mul__(calc2))
        elif choice == 10:
            print("Result: ", calc1.__truediv__(calc2))
        elif choice == 11:
            print("Result of operation: ", cn3)
        elif choice == 0:
            print("Exiting!")
        else:
            print("Invalid choice!!")


menu()
