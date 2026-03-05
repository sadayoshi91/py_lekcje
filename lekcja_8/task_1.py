# ZADANIE 1 

wynik = None
try:
        a = float(input("Podaj pierwszą liczbę: "))
        znak = input("Podaj działanie (+, -, *, /): ")
        b = float(input("Podaj drugą liczbę: "))

        if znak == "+":
            wynik = a + b
            print("Wynik:", wynik)

        elif znak == "-":
            wynik = a - b
            print("Wynik:", wynik)

        elif znak == "*":
            wynik = a * b
            print("Wynik:", wynik)

        elif znak == "/":
            wynik = a / b
            print("Wynik:", wynik)

        else:
            print("Nieznane działanie!")

except ValueError: # obsługa wyjątku wartości - jeżeli podamy coś innego niż liczba to wywoła ten komunikat
    print("Błąd - podaj poprawne liczby")
except ZeroDivisionError: # obsługa wyjątku dzielenia przez zero - wyświetla komunikat jeżeli w działaniu podzielimy przez 0 liczby / jest to wbudowana funkcja pythona
    print("Błąd! Nie można dzielić przez zero")
else:
    print(f"Wynik: {wynik}") # wyświetlenie wyniku
finally:
    print("Kolejna operacja...") # kontynuacja mimo znalezienia któregoś z powyższych błędów