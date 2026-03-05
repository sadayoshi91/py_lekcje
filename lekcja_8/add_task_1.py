# Bezpieczna konwersja
# Napisz funkcję bezpieczny_int(tekst) zwracającą liczbę całkowitą lub None, jeśli konwersja się
# nie uda. Użyj try/except ValueError.
# Wskazówka: try: return int(tekst) / except ValueError: return None.

def safe_int(some_text):
    try:
        return int(some_text)
    except ValueError:
        return None
    
print(safe_int("123"))  # Zwraca 123
print(safe_int("abc"))  # Zwraca None