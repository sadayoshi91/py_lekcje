# Napisz dekorator @wymaga_int, który przed wywołaniem funkcji sprawdza, czy wszystkie
# argumenty pozycyjne (*args) są typu int. Jeśli nie — wyświetla komunikat "Błąd: wszystkie
# argumenty muszą być liczbami całkowitymi!" i nie wywołuje funkcji.
# Wskazówka: W wrapper sprawdź: all(isinstance(a, int) for a in args). Funkcja all() zwraca True,
# jeśli wszystkie elementy są True.

def req_int(func):

    def wrapper(*args, **kwargs):
        if not all(isinstance(a, int) for a in args):
            print("Błąd: wszystkie argumenty muszą być liczbami całkowitymi!")
            return 
        return func(*args, **kwargs)
    return wrapper
    
@req_int
def new_func(a, b):
    return a + b

print(new_func(1, 3)) # ok
print(new_func(1, "19")) # nok
print(new_func(1, 9.2)) # nok
