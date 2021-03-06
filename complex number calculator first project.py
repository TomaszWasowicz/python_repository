class Complex (object):
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
        print(f"Number is erased: {(self.real, self.imaginary)}")

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
#class Calculator(Complex):

    def __add__(self, other):
        result_real = self.real+other.real
        result_imaginary = self.imaginary+other.imaginary
        result = Complex(result_real, result_imaginary)
        return result

    def __sub__(self, other):
        result_real = self.real-other.real
        result_imaginary = self.imaginary-other.imaginary
        result = Complex(result_real, result_imaginary)
        return result

    def __mul__(self, other):
        result_real = (self.real*other.real-self.imaginary*other.imaginary)
        result_imaginary = (self.real*other.imaginary+other.real*self.imaginary)
        result = Complex(result_real, result_imaginary)
        return result

    def __truediv__(self, other):
        result_real = float(float(self.real*other.real+self.imaginary*other.imaginary)/float(other.real*other.real+other.imaginary*other.imaginary))
        result_imaginary = float(float(other.real*self.imaginary-self.real*other.imaginary)/float(other.real*other.real+other.imaginary*other.imaginary))
        result = Complex(result_real, result_imaginary)
        return result


c1 = Complex(0, 0)
c2 = Complex(0, 0)

#calc1 = Calculator(c1, c2)

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
    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Result: ", c1.create_number())
    elif choice == 2:
        print("Result: ", c2.create_number())
    elif choice == 3:
        print("Result: ", c1.display_number())
    elif choice == 4:
        print("Result: ", c2.display_number())
    elif choice == 5:
        print("Result: ", c1.erase_number())
    elif choice == 6:
        print("Result: ", c2.erase_number())
    elif choice == 7:
        print("Result: ", c1.__add__(c2))
    elif choice == 8:
        print("Result: ", c1.__sub__(c2))
    elif choice == 9:
        print("Result: ", c1.__mul__(c2))
    elif choice == 10:
        print("Result: ", c1.__truediv__(c2))
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
