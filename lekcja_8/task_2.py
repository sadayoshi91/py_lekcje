## Zadanie 2

# Walidator wieku: Stwórz funkcję rejestruj_uzytkownika(wiek) , która rzuca własnym,
# zdefiniowanym przez Ciebie wyjątkiem WiekNiepoprawnyError , jeśli wiek jest mniejszy niż
# 18. Napisz kod, który wywołuje tę funkcję i obsługuje ten wyjątek.

class WiekNiepoprawnyError(Exception):
    pass

def rejestruj_uzytkownika(wiek):
    if wiek < 18:
        raise WiekNiepoprawnyError("Podano niepoprawny wiek")
    else:
        print(f"Twój wiek to {wiek}")

age = int(input("Podaj wiek"))

try:
    rejestruj_uzytkownika(age)
except WiekNiepoprawnyError as error:
    print(f"Wystąpił błąd: {error}")