# Napisz funkcję statystyki(*args) zwracającą krotkę: (ilość, suma, średnia). Obsłuż przypadek
# pustych argumentów (zwróć 0, 0, 0).
# Wskazówka: len(args), sum(args), sum/len. Rozpakuj wynik: ilosc, suma, sr = statystyki(1, 2, 3).

def stats(*args) -> tuple:
    if not args:
        return 0, 0, 0
    return len(args), sum(args), sum(args) / len(args)

# test nr1
quantity, total, avg = stats(1, 2, 3)

print("Test 1:")
print("Ilość:", quantity)
print("Suma:", total)
print("Średnia:", avg)
print("-" * 40)

# test nr2
quantity, total, avg = stats(10, 20, 30, 40)

print("Test 2:")
print("Ilość:", quantity)
print("Suma:", total)
print("Średnia:", avg)
print("-" * 40)

# test nr3
quantity, total, avg = stats()

print("Test 3 (puste argumenty):")
print("Ilość:", quantity)
print("Suma:", total)
print("Średnia:", avg)