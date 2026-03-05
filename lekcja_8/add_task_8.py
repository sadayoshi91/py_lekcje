# Napisz funkcję waliduj_formularz(dane) przyjmującą słownik. Zbierz błędy do listy:
# Brak klucza "imie" lub puste imie -- blad
# Brak klucza "email" lub brak "@" w emailu -- blad
# Brak klucza "wiek" lub wiek < 0 -- blad
# Jeśli są błędy, rzuć BladWalidacjiError(bledy). Użyj .get() do bezpiecznego dostępu.
# Wskazówka: Użyj dane.get("imie", "") do pobrania wartości domyślnej. Sprawdzaj każdy
# warunek i dodawaj do listy bledy.

class BladWalidacjiError(Exception):
    def __init__(self, bledy):
        self.bledy = bledy
        super().__init__("Błędy walidacji: " + ", ".join(bledy))
        
def waliduj_formularz(dane):
    bledy = []
    imie = dane.get("imie", "")
    if not imie:
        bledy.append("Brak imienia")
    email = dane.get("email", "")
    if "@" not in email:
        bledy.append("Nieprawidłowy email")
    wiek = dane.get("wiek", -1)
    if wiek < 0:
        bledy.append("Nieprawidłowy wiek")
    if bledy:
        raise BladWalidacjiError(bledy)
    return True

# Przykładowe testy
try:    waliduj_formularz({"email": "janexample.com", "wiek": -5})
except BladWalidacjiError as e:    print(e)
try:    waliduj_formularz({"imie": "", "email": "jan    @example.com"})
except BladWalidacjiError as e:    print(e) 
try:    waliduj_formularz({"imie": "Jan", "email": "jan@example.com", "wiek": 25})
except BladWalidacjiError as e:    print(e)