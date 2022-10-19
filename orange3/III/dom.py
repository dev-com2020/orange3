import random

class Dom:
    kolor = None
    ilosc_okien = None
    czy_ma_basen = False

    def buduj_basen(self):
        self.czy_ma_basen = True
        print("Basen został zbudowany")

    def maluj_dom(self):
        kolory = ["biały", "zielony", 'czerwony']
        self.kolor = random.choice(kolory)
        print("Dom pomalowany na __kolor:", self.kolor)

    def wstaw_okna(self):
        self.ilosc_okien = random.randint(1, 6)
        print("wstawiam okna w ilości:", self.ilosc_okien)


