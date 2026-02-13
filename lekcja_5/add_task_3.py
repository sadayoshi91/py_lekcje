# Poproś o słowo. Wyświetl jego litery od ostatniej do pierwszej, każdą w osobnej linii z indeksem
# od końca.
# Wskazówka: Użyj slicing \[::-1\] z enumerate(), albo range(len(slowo)-1, -1, -1)

word = input("Podaj dowolne słowo: ")[::-1]
# word_before = word[::-1] - nie wiem czy opłaca się dzielnić na kolejną zmienną 
# użyć enumerate zamiast range - bardziej czytelny kod
for index, word in enumerate(word):
    print(f"{index}: {word}", end=", ")