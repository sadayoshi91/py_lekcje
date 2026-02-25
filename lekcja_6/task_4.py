# Sprawdzanie zakresu: Zdefiniuj zmienną globalną POZIOM_DOSTEPU = "user" . Napisz
# funkcję, która próbuje zmienić tę zmienną na "admin" bez użycia słowa kluczowego
# global . Wewnątrz funkcji stwórz zmienną lokalną o tej samej nazwie. Wyświetl wartość
# zmiennej wewnątrz i na zewnątrz funkcji, aby zobaczyć różnicę.

ACCES_LEVEL = "user"

def change_glob():
    ACCES_LEVEL = "admin"
    print(f"W funkcji: {ACCES_LEVEL}")

change_glob()
print(f"Poza funkcją: {ACCES_LEVEL}")

# bez słowa kluczowego global python traktuje przypisanie jako tworzenie zmiennej lokalnej 
