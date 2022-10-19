import time


def wykonaj(funkcja, a, b):
    x = funkcja(a, b)
    return x


def dodaj(a, b):
    print("wynik=", a + b)


def odejmij(a, b):
    print("wynik=", a - b)


dodaj(4, 5)
wykonaj(dodaj, 4, 5)


def glowna():
    def wewnetrzna(a, b):
        return a * b

    x = wewnetrzna(2, 3)
    return x


print(glowna())


def dekorTomka(funkcja):
    def wew(*args, **kwargs):
        start = time.time()
        x = funkcja(*args, **kwargs)
        koniec = time.time()
        print(funkcja.__name__, "wykonała się", koniec - start, "sek.")
        return x

    return wew


@dekorTomka
def zwykla(a, b, c):
    print("Ja sobie tutaj robię swoje...")
    time.sleep(2)
    print(a + b + c)


@dekorTomka
def zwykla2(a, b):
    time.sleep(2.5)
    print("Ja sobie tutaj robię swoje...")
    print(a + b)


zwykla(4, 5, 6)
zwykla2(4, 5)
