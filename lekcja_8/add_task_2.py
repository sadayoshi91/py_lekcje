# Bezpieczne dzielenie
# Napisz funkcję podziel(a, b) zwracającą wynik dzielenia. Jeśli b == 0, zamiast błędu zwróć tekst
# "Nie można dzielić przez zero". Użyj try/except ZeroDivisionError.

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Nie można dzielić przez zero"
    
print(divide(10, 2))  # Zwraca 5.0
print(divide(10, 0))  # Zwraca "Nie można dzielić przez zero"
