zmienna = lambda x, y: x + y
print(zmienna(3, 4))

zmienna2 = lambda _: _ + 1
print(zmienna2(5))
print(zmienna2(55))
print(zmienna2(57))

lista = [1, 5, 7, 9]
print(f"Zastosowanie filtra: {list(map(lambda l: l * 3, lista))}")
print(f"Zastosowanie filtra: {list(filter(lambda l: l > 3, lista))}")
