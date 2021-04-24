import unittest                                         #moduł testowy
from datetime import datetime, timedelta                #moduł data/czas
from bike_rental_shop import BikeRental, Customer             #moduł klasy bikeRental


class BikeRentalTest(unittest.TestCase):                        #test wypożyczeń - liczba rowerów dostępnych
    def test_Bike_Rental_displays_correct_stock(self):
        shop1 = BikeRental(4)                                    #obiekt sklep1
        shop2 = BikeRental(20)                                  #obiekt sklep2
        self.assertEqual(shop1.displaystock(), 4)
        self.assertEqual(shop2.displaystock(), 20)

    def test_rentBikeOnHourlyBasis_for_negative_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnHourlyBasis(-1), None)

    def test_rentBikeOnHourlyBasis_for_zero_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnHourlyBasis(0), None)

    def test_rentBikeOnHourlyBasis_for_valid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentBikeOnHourlyBasis(2).hour, hour)

    def test_rentBikeOnHourlyBasis_for_invalid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnHourlyBasis(11), None)

    def test_rentBikeOnDailyBasis_for_negative_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnDailyBasis(-1), None)

    def test_rentBikeOnDailyBasis_for_zero_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnDailyBasis(0), None)

    def test_rentBikeOnDailyBasis_for_valid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentBikeOnDailyBasis(2).hour, hour)

    def test_rentBikeOnDailyBasis_for_invalid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnDailyBasis(11), None)

    def test_rentBikeOnWeeklyBasis_for_negative_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnWeeklyBasis(-1), None)

    def test_rentBikeOnWeeklyBasis_for_zero_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnWeeklyBasis(0), None)

    def test_rentBikeOnWeeklyBasis_for_valid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentBikeOnWeeklyBasis(2).hour, hour)

    def test_rentBikeOnWeeklyBasis_for_invalid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnWeeklyBasis(11), None)

    def test_returnBike_for_invalid_rentalTime(self):                       # stwórz sklep i klienta
        shop = BikeRental(10)
        customer = Customer()
        request = customer.returnBike()                                     # pozwól klientowi nie wypożyczyć roweru, a potem go zwrócić
        self.assertIsNone(shop.returnBike(request))                         # manualnie sprawdz co funckja zwraca z 'error values' - błędnymi wartościami
        self.assertIsNone(shop.returnBike((0, 0, 0)))

    def test_returnBike_for_invalid_rentalBasis(self):                      # stwórz sklep i klienta
        shop = BikeRental(10)
        customer = Customer()
        customer.rentalTime = datetime.now()                                # stwórz właściwy czas wypożyczenia i rowery
        customer.bikes = 3
        customer.rentalBasis = 7                                            # stwórz niewłaściwą bazę wypożyczeń
        request = customer.returnBike()
        self.assertEqual(shop.returnBike(request), 0)

    def test_returnBike_for_invalid_numOfBikes(self):
        shop = BikeRental(10)                                               # stwórz sklep i klienta
        customer = Customer()
        customer.rentalTime = datetime.now()                                # stwórz właściwy czas wypożyczenia i bazę wypożyczeń
        customer.rentalBasis = 1
        customer.bikes = 0                                                  # stwórz 'niewłaściwe' obiekty - rowery
        request = customer.returnBike()
        self.assertIsNone(shop.returnBike(request))

    def test_returnBike_for_valid_credentials(self):                        # stwórz sklep i różnych klientów
        shop = BikeRental(50)
        customer1 = Customer()
        customer2 = Customer()
        customer3 = Customer()
        customer4 = Customer()
        customer5 = Customer()
        customer6 = Customer()

        customer1.rentalBasis = 1  # godz                 # stwórzy właściwą bazę wypożyczeń dla każdego klienta
        customer2.rentalBasis = 1  # godz
        customer3.rentalBasis = 2  # dzien
        customer4.rentalBasis = 2  # dzien
        customer5.rentalBasis = 3  # tydzien
        customer6.rentalBasis = 3  # tydzien

        customer1.bikes = 1                                 # stwórz 'właściwe' obiekty - rowery dla każdego klienta
        customer2.bikes = 5                                   # pasuje do rodzinnej zniżki 30%
        customer3.bikes = 2
        customer4.bikes = 8
        customer5.bikes = 15
        customer6.bikes = 30

        customer1.rentalTime = datetime.now() + timedelta(hours=-4)     # stwórz przeszłe właściwe czasy wypożyczeń dla każdego klienta
        customer2.rentalTime = datetime.now() + timedelta(hours=-23)
        customer3.rentalTime = datetime.now() + timedelta(days=-4)
        customer4.rentalTime = datetime.now() + timedelta(days=-13)
        customer5.rentalTime = datetime.now() + timedelta(weeks=-6)
        customer6.rentalTime = datetime.now() + timedelta(weeks=-12)

        request1 = customer1.returnBike()                               # spraw by wszyscy klienci zwrócili rowery
        request2 = customer2.returnBike()
        request3 = customer3.returnBike()
        request4 = customer4.returnBike()
        request5 = customer5.returnBike()
        request6 = customer6.returnBike()

        self.assertEqual(shop.returnBike(request1), 20)                 # sprawdz, czy wszyscy dostali właściwy rachunek
        self.assertEqual(shop.returnBike(request2), 402.5)
        self.assertEqual(shop.returnBike(request3), 160)
        self.assertEqual(shop.returnBike(request4), 2080)
        self.assertEqual(shop.returnBike(request5), 5400)
        self.assertEqual(shop.returnBike(request6), 21600)


class CustomerTest(unittest.TestCase):

    def test_return_Bike_with_valid_input(self):

        customer = Customer()                                   # stwórz klienta

        now = datetime.now()                                    # stwórz właściwy czas wypożyczenia, bazę wypożyczeń, rowery
        customer.rentalTime = now
        customer.rentalBasis = 1
        customer.bikes = 4
        self.assertEqual(customer.returnBike(), (now, 1, 4))

    def test_return_Bike_with_invalid_input(self):

        customer = Customer()                                   # stwórz klienta

        customer.rentalBasis = 1                                # stwórz właściwą bazę wypożyczeń i rowery
        customer.bikes = 0

        customer.rentalTime = 0                                 # stwórz niewłaściwy czas wypożyczenia
        self.assertEqual(customer.returnBike(), (0, 0, 0))


if __name__ == '__main__':
    unittest.main()