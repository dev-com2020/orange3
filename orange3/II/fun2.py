# name = "Aga"
#
# def get_name():
#     global name
#     name = input("Podaj imię: ")
#
# get_name()
# print("Witaj", name)
import random


# def get_name():
#     name = input("Podaj imię: ")
#     return name
#
# name = get_name()
#
# print("Witaj", name.upper())

def mam_global(a):
    # global a
    suma = 5 + a
    return suma


# print(mam_global(5))

# random.seed(5)

cyfra = random.randint(1, 6) * 2
print("Wylosowana cyfra to: ", cyfra)

cyfra2 = random.random() * 1000
print(cyfra2)

cyfra3 = random.randrange(1, 100, 5)
print(cyfra3)

wiek = [33, 43, 32, 555, 777, 333]

print(random.choice(wiek))