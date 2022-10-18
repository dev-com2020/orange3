imie = "Jarek"
wiek = [33, 43, 32]
imiona = []
print(imiona)
imiona.append("Tomek")
imiona.append("Jacek")
imiona.append(123)
imiona.append(imie)
imiona.insert(1, "Piotr")
imiona.append(wiek)
imie = "Aga"
imiona.pop()
imiona.remove(123)
print(imiona[0], imiona[3], imiona[-1][1])
# imiona[0] = input("Podaj imię!")
# print(imiona)
# print(len(imiona))
imiona.sort()
# print(imiona)
# print(imiona[0])
imiona2 = imiona.copy() # kopia bezpieczeństwa, obecnie zastepowana przez pickle()
imiona3 = imiona2 #odwołanie sie po innej nazwie do tego samego obiektu!
imiona.pop()
print(imiona)
print(imiona2)
print(imiona[:2])
lista3 = wiek + imiona2
print(len(lista3))

numbers = [10, 34] * 5
print(numbers)
del numbers[2]

print(max(numbers))
print(min(numbers))
print(sum(numbers))
#
#
# for i in numbers:
#     print(i)
