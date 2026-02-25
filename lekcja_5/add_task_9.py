# Utwórz słownik z 5 słowami polskimi jako kluczami i ich angielskimi tłumaczeniami jako
# wartościami. W pętli while True: użytkownik wpisuje polskie słowo, program wyświetla
# tłumaczenie. Wpisanie "quit" kończy program. Jeśli słowa nie ma w słowniku — "Nie znam tego
# słowa".
# Wskazówka: Słownik tlumaczenia = {"kot": "cat", ...}. Sprawdź if slowo in tlumaczenia.

polish_translate = {"czerwony": "red","kwiat": "flower","młotek": "hammer", "narzedzia": "tools","mysz": "mouse"}

# uznałem, że ładnie będzie podzielić każde zdanie na osobny wiersz
print("Witaj w tłumaczu!\n"
      "Wybierz 5 słów z poniższej listy do przetłumaczenia:\n"
      "czerwony, kwiat, młotek, narzędzia, mysz\n"
      "Aby zakończyć program wpisz QUIT")

while True:
    word = input("Podaj słowo: ").lower()
    if word == "quit":
        break
    # użyłem .get aby kod był możliwie krótki i przejrzysty 
    print(f"Tłumaczenie słowa to: ", polish_translate.get(word, "Nieprawidłowe słowo!"))




