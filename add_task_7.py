# Napisz domknięcie stworz_pozdrowienie(jezyk), które zwraca funkcję. Dla jezyk="pl" zwrócona
# funkcja mówi "Cześć, {imie}!", dla "en" — "Hello, {imie}!". Użyj bez nonlocal (jezyk jest tylko
# odczytywany).
# Wskazówka: Funkcja wewnętrzna "pamięta" wartość jezyk z zakresu otaczającego. Użyj if/elif
# wewnątrz.

def create_greetings(language):

    def wrapper(name):
        if language == "pl":
            return f"Cześć, {name}!"
        elif language == "en":
            return f"Hello, {name}!"

    return wrapper