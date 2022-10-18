def fun1(*cyfry, **kwargs):
    lista = []
    print(kwargs)
    print("Liczba argumentów", len(cyfry))
    for i in cyfry:
        print("Wartość:", i)
        lista.append(i)
    return lista


fun1(34, imie="Tomek")
fun1(3, 4)
fun1(3, 5, 8)
lista = fun1(5, 6, 7)
print(lista)
