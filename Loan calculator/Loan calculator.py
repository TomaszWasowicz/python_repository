from tkinter import *


class LoanCalculator:

    def __init__(self):
        window = Tk()                                                                                   # Stwórz okno
        window.title("Kalkulator pożyczkowy")                                                           # Tytuł okna programu

        Label(window, text="Roczna stopa procentowa").grid(row=1, column=1, sticky=W)                   # Okna inputu
        Label(window, text="Ilosc lat do spłaty kredytu").grid(row=2, column=1, sticky=W)
        Label(window, text="Wysokosc kredytu").grid(row=3, column=1, sticky=W)
        Label(window, text="Miesieczna rata kredytu").grid(row=4, column=1, sticky=W)
        Label(window, text="Całkowity koszt kredytu").grid(row=5, column=1, sticky=W)

        self.annualInterestRateVar = StringVar()                                                         # metody do przyjmowania danych wejsciowych
        Entry(window, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=1, column=2)
        self.numberOfYearsVar = StringVar()

        Entry(window, textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=2, column=2)
        self.loanAmountVar = StringVar()

        Entry(window, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=3, column=2)
        self.monthlyPaymentVar = StringVar()
        Label(window, textvariable=self.monthlyPaymentVar).grid(row=4, column=2, sticky=E)

        self.totalPaymentVar = StringVar()
        Label(window, textvariable=self.totalPaymentVar).grid(row=5, column=2, sticky=E)

        Button(window, text="Oblicz szczegóły płatności", command=self.compute_payment).grid(row=6, column=2, sticky=E)
        window.mainloop()                                                                                   #stwórz onko z pętlą wydarzenia

    def compute_payment(self):                                                                              #obliczanie kosztów kredytu
        monthly_payment = self.get_monthly_payment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberOfYearsVar.get()))

        self.monthlyPaymentVar.set(format(monthly_payment, '10.2f'))
        total_payment = float(self.monthlyPaymentVar.get()) * 12 \
                       * int(self.numberOfYearsVar.get())

        self.totalPaymentVar.set(format(total_payment, '10.2f'))

    @staticmethod
    def get_monthly_payment(loan_amount, monthly_interest_rate, number_of_years):                        #oblicz miesięczną płatność

        monthly_payment = loan_amount * monthly_interest_rate / (1 - 1 / (1 + monthly_interest_rate) ** (number_of_years * 12))
        return monthly_payment


LoanCalculator()
