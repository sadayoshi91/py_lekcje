#  Logowanie do pliku
# Napisz funkcję zaloguj_blad(komunikat, plik="log.txt") która dopisuje komunikat do pliku. Użyj
# trybu "a" i with open(). Przetestuj, wywołując ją kilka razy.
# Wskazówka: with open(plik, "a") as f: f.write(komunikat + "\\n").

def set_error(komunikat, plik="log.txt"):
    with open(plik, "a", encoding="utf-8") as f:
        f.write(komunikat + "\n")

set_error("Błąd: Nie można połączyć z bazą danych.")
set_error("Błąd: Nie można znaleźć pliku konfiguracyjnego.")
set_error("Błąd: Nie można odczytać dane z API.")    