import datetime


class BikeRental:

    def __init__(self, stock=0):                    # klasa konstruckyjna inicjalizująca klasę bike rental
        self.stock = stock

    def displaystock(self):                         # funkcja wyświetląjąca rowery, które można wypożyczyć
        print("We have currently {} bikes available to rent.".format(self.stock))
        return self.stock

    def rentBikeOnHourlyBasis(self, n):            # godzinne wypożyczenie roweru klientowi
        if n <= 0:                                 # odmowa / odrzucenie niewłaściwego inputu danych
            print("Number of bikes should be positive!")
            return None                             # nie wypożyczaj klientowi roweru, jeśli stan jest mniejszy od żądanej ilości wypożyczonych rowerów
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        else:                                       # wypożycz rowery
            now = datetime.datetime.now()
            print("You have rented a {} bike(s) on hourly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $5 for each hour per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now

    def rentBikeOnDailyBasis(self, n):              # dzienne wypożyczanie rowerów klientowi
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on daily basis today at {} hours.".format(n, now.hour))
            print("You will be charged $20 for each day per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now

    def rentBikeOnWeeklyBasis(self, n):             # tygodniowe wypożyczenie klientowi rowerów
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on weekly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $60 for each week per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now

    def returnBike(self, request):                          # 1. przyjmuj wypożyczony rower od klienta, 2. uzupełnij zapas rowerów, 3. zwróć rachunek
        rentalTime, rentalBasis, numOfBikes = request        # extract the tuple and initiate bill
        bill = 0
        if rentalTime and rentalBasis and numOfBikes:       # wystaw rachunek tylko wtedy, gdy wszystkie 3 parametry nie są pełne
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime
            if rentalBasis == 1:                            # godzinna kalkulacja rachunku
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes
            elif rentalBasis == 2:                          # dzienna kalkulacja rachunku
                bill = round(rentalPeriod.days) * 20 * numOfBikes
            elif rentalBasis == 3:                          # tygodniowa kalkulacja rachunku
                bill = round(rentalPeriod.days / 7) * 60 * numOfBikes
            if (3 <= numOfBikes <= 5):                      # zniżka rodzinna
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7
            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            return bill

        else:
            print("Are you sure you rented a bike with us?")
            return None


class Customer:
    def __init__(self):                     # metoda konstrukcyjna, która wywołuje różne obiekty związane z klientem
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestBike(self):                  #Przyjmuj zgłoszenie od klienta o liczbie rowerów
        bikes = input("How many bikes would you like to rent?")
        try:                                # wyjątek w razie niewłaściwego inputu danych
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1
        if bikes < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes

    def returnBike(self):                   # Pozwól klientowi zwrócić rowery do wypożyczalni.
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes
        else:
            return 0, 0, 0

