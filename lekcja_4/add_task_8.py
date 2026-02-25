# Program pyta o dwie liczby i operację (+, -, *, /). Wyświetla wynik. Jeśli użytkownik wybierze
# dzielenie i poda 0 jako drugą liczbę, wyświetla komunikat "Nie można dzielić przez zero!"
# zamiast wyniku.
# Wskazówka: Sprawdź warunek b == 0 PRZED wykonaniem dzielenia. Użyj if/elif/else.

number_1 = int(input("Podaj liczbę nr1: "))
number_2 = int(input("Podaj liczbę nr2: "))

sum = input("Podaj znak działania (+ - / *)")

if sum == "+":
    print(f"Wynik dodawania {number_1 + number_2}")
elif sum == "-":
    print(f"Wynik odejmowania {number_1 - number_2}")
elif sum == "*":
    print(f"Wynik mnożenia{number_1 * number_2}")
elif sum == "/":
    if number_2 == 0:
        print("Nie można dzielić przez 0")
    else: 
        print(f"Wynik dzielenia {number_1 / number_2}")