class Ptak:
    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print("Tu", self.gatunek, "lecę i osiągam prędkość max: ", self.szybkosc)

    def wydajOdglos(self):
        pass


class Kura(Ptak):

    def idz_na_rosol(self):
        print("Idę na rosół!")

    def wydajOdglos(self):
        print("kokokoko")


