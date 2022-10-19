from abc import ABC, abstractmethod


class Ptak(ABC):
    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print("Tu", self.gatunek, "lecę i osiągam prędkość max: ", self.szybkosc)

    @abstractmethod
    def wydajOdglos(self):
        pass


class Kura(Ptak):

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def idz_na_rosol(self):
        print("Idę na rosół!")

    def wydajOdglos(self):
        print("kokokoko")

    def lataj(self):
        print("Tu", self.gatunek, "ja nie latam, ale sobie pobiegam!")

class Pingwin(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)
    def lataj(self):
        print("Tu", self.gatunek, "ja nie latam, ale sobie pobiegam!")

    def wydajOdglos(self):
        print("piiiii")

    @staticmethod
    def formatowanie():
        return "test"
    @classmethod
    def licznik(cls):
        print("ja sobie działam niezależnie!")