# Napisz program, który odczytuje plik config.json z poprzedniego
# zadania i wyświetla komunikat: Witaj, [uzytkownik]! Twój motyw to [motyw].

import json
try:
    with open("lekcja_9/config.json", "r", encoding="utf-8") as file:
        config = json.load(file)
        print(f"Witaj, {config['uzytkownik']}! Twój motyw to {config['motyw']}.")
except FileNotFoundError:
    print("Plik config.json nie został znaleziony.")
    print("Upewnij się, że plik istnieje w katalogu lekcja_9.")