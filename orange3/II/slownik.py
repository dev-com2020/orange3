slownik = {1: "Tomek",
           2: "Jarek",
           "imie": "Aga",
           "rok": 1988
           }

print(slownik[1])
slownik["rok"] = 2022
slownik["godzina"] = 11
slownik["tabela"] = [5, 3, 4, 6, 3, 66]
print(slownik["imie"])
print(slownik["rok"])
print(slownik.items())
print(slownik.keys())
print(slownik.values())

if "rok" in slownik:
    print(slownik["rok"])
if "rok2" not in slownik:
    print("Nie znaleziono klucza o wartości rok2")
