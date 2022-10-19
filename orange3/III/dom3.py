import random


class Dom:

    def __init__(self, kolor, ilosc_okien, czy_ma_basen=False):
        self.__kolor = kolor
        self.__ilosc_okien = ilosc_okien
        self.__czy_ma_basen = czy_ma_basen

    def buduj_basen(self):
        self.__czy_ma_basen = True
        print("Basen został zbudowany")

    def maluj_dom(self):
        print("Dom pomalowany na kolor:", self.__kolor)

    def wstaw_okna(self):
        print("wstawiam okna w ilości:", self.__ilosc_okien)
