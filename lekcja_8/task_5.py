log_file = None
try:
    log_file = open("lekcja_8/log.txt",
                    mode='a')
except FileNotFoundError:
    print("Plik nie istnieje")

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
        print("Nieznane działanie!")
        wynik = None
        
except ValueError:
    print("Błąd - podaj poprawne liczby")
    if log_file is not None:
        log_file.write("Błąd - podaj poprawne liczby\n")
except ZeroDivisionError:
    print("Błąd! Nie można dzielić przez zero")
    if log_file is not None:
        log_file.write("Błąd! Nie można dzielić przez zero\n")
else:
    if wynik is not None:
        print(f"Wynik: {wynik}")
        if log_file is not None:
            log_file.write(f"Wynik: {wynik}\n")
finally:
    print("Kolejna operacja...")
    if log_file is not None:
        log_file.close()