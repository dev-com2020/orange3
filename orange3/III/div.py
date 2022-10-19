# def dzielenie():
#     num1 = int(input("Podaj 1 liczbę:"))
#     num2 = int(input("Podaj 2 liczbę:"))
#     if num2 != 0:
#         wynik = num1 / num2
#         print(num1, 'dzielone przez', num2, 'daje', wynik)
#     else:
#         print("Nie można dzielić przez zero")


# def dzielenie():
#     try:
#         num1 = int(input("Podaj 1 liczbę:"))
#         num2 = int(input("Podaj 2 liczbę:"))
#         wynik = num1 / num2
#         print(num1, 'dzielone przez', num2, 'daje', wynik)
#     except ZeroDivisionError:
#         print("😩 nie można dzielić przez zero, spróbuj ponownie...😩")
#     except ValueError:
#         print("😩 podano nieprawidłowe dane, spróbuj ponownie...😩")

# def dzielenie():
#     try:
#         num1 = int(input("Podaj 1 liczbę:"))
#         num2 = int(input("Podaj 2 liczbę:"))
#         wynik = num1 / num2
#         print(num1, 'dzielone przez', num2, 'daje', wynik)
#     except (ZeroDivisionError, ValueError):
#         print("😩 wystapił błąd, spróbuj ponownie...😩")

def dzielenie():
    try:
        num1 = int(input("Podaj 1 liczbę:"))
        num2 = int(input("Podaj 2 liczbę:"))
        wynik = num1 / num2
    except Exception as e:
        print("😩 wystapił błąd=", e, "spróbuj ponownie...😩")
    else:
        print(num1, 'dzielone przez', num2, 'daje', wynik)
    finally:
        print("---Dziękujemy za skorzystanie z naszego programu!---")



while True:
    dzielenie()
