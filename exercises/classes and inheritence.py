# Program
# Napisany przez Tomasza Wąsowicza

class Animal:
    def move(self):
        print("I am moving slowly")
    def eat(self):
        print("mniam mniam")

class Dog(Animal):
    def move(self):
        print("I am moving fast")


class Bird(Animal):
    def move(self):
        print("I am flying")
    def voice(self):
        #pass motoda nic nie robi
        print("cwir cwir")


class DogBird(Dog, Bird):
    def i_am_weirdo(self):
        print("wtf")


burek = Dog()

elemelek = Bird()
dziwny = DogBird()
dziwny.i_am_weirdo()
#zadanie: dodac metode "eat", pioes je mieso, ptak je ziarno, kotopies je?
dziwny.eat()
dziwny.voice()
