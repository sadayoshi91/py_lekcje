# Stwórz słownik Pythona z ustawieniami aplikacji, np.
# konfiguracja = {"uzytkownik": "admin", "motyw": "ciemny", "rozdzielczosc":
# [1920, 1080]} . Zapisz ten słownik do pliku config.json z wcięciami i poprawnym
# kodowaniem polskich znaków.

# json zaimportowane w celu zapisania słownika do pliku json, który jest formatem tekstowym, który jest łatwy do odczytania i zapisu danych strukturalnych.
import json

config = {"uzytkownik": "admin", "motyw": "ciemny", "rozdzielczosc": [1920, 1080]}

with open("lekcja_9/config.json", "w", encoding="utf-8") as file:
    json.dump(config, file, ensure_ascii=False, indent=4)
    print("Konfiguracja zapisana do pliku config.json")


