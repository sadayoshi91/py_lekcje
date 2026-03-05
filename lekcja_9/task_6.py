# Napisz program, który odczytuje plik produkty.csv i oblicza sumę cen
# wszystkich produktów. Użyj csv.DictReader , aby łatwiej odwoływać się do kolumn po
# nazwach.

import csv
try:
    with open("lekcja_9/produkty.csv", mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        total_price = sum(float(row["cena"]) for row in reader)
        print(f"Suma cen wszystkich produktów: {total_price:.2f}")
except FileNotFoundError:
    print("Plik produkty.csv nie został znaleziony.")
    print("Upewnij się, że plik istnieje w katalogu lekcja_9.")
except KeyError:
    print("Plik produkty.csv nie zawiera kolumny 'cena'.")
except ValueError:
    print("Nie można przekonwertować wartości ceny na liczbę. Upewnij się, że wszystkie ceny są poprawne.")
finally:
    print("Koniec programu.")
    