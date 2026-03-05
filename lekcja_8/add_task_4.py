# Pobieranie liczby z walidacją
# Napisz funkcję pobierz_liczbe_z_zakresu(minimum, maksimum) która w pętli prosi o liczbę. Jeśli
# nie jest liczbą — ValueError. Jeśli poza zakresem — wyświetl komunikat i pytaj ponownie. Użyj
# else do potwierdzenia sukcesu.
# Wskazówka: while True + try/except ValueError + if/else do sprawdzenia zakresu.

def get_number_in_range(minimum, maximum):
    while True:
        try:
            number = float(input(f"Podaj liczbę z zakresu {minimum} - {maximum}: "))
            if minimum <= number <= maximum:
                print("Dziękuję za podanie poprawnej liczby!")
                return number
            else:
                print(f"Podana liczba jest poza zakresem {minimum} - {maximum}. Spróbuj ponownie.")
        except ValueError:
            print("To nie jest poprawna liczba. Spróbuj ponownie.")

result = get_number_in_range(1, 10)
print(f"Podana liczba to: {result}")
