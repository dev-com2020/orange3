import random


class Dom:

    def __init__(self, kolor, ilosc_okien, czy_ma_basen=False):
        self.kolor = kolor
        self.ilosc_okien = ilosc_okien
        self.czy_ma_basen = czy_ma_basen

    def buduj_basen(self):
        self.czy_ma_basen = True
        print("Basen został zbudowany")

    def maluj_dom(self):
        print("Dom pomalowany na __kolor:", self.kolor)

    def wstaw_okna(self):
        print("wstawiam okna w ilości:", self.ilosc_okien)
