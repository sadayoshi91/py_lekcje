#  Kalkulator z logowaniem
# Napisz kalkulator (zadanie 1), ale każdy błąd loguj do pliku "kalkulator_log.txt" zamiast
# wyświetlać. Użyj funkcji z ćwiczenia S6.
# Wskazówka: W except: zaloguj_blad(str(e)).

def set_error(komunikat, plik="kalkulator_log.txt"):
    with open(plik, "a", encoding="utf-8") as f:
        f.write(komunikat + "\n")
try:
    a = float(input("Podaj pierwszą liczbę: "))
    znak = input("Podaj działanie (+, -, *, /): ")
    b = float(input("Podaj drugą liczbę: "))

    if znak == "+":
        wynik = a + b
    elif znak == "-":
        wynik = a - b
    elif znak == "*":
        wynik = a * b
    elif znak == "/":
        wynik = a / b
    else:
        raise ValueError("Nieznane działanie!")
except ValueError as e:
    set_error(f"Błąd - {str(e)}")
except ZeroDivisionError as e:
    set_error(f"Błąd! Nie można dzielić przez zero - {str(e)}")
else:
    print(f"Wynik: {wynik}")
