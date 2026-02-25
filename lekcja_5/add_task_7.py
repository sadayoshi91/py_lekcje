# Wyświetl tablicę dzielenia: dla i od 1 do 5 i j od 1 do 5 wyświetl i/j z dwoma miejscami po
# przecinku. Wyrównaj do ładnej tabelki.
# Wskazówka: Zagnieżdżone pętle jak w sekcji 2.4. Użyj f"{i/j:6.2f}" dla wyrównania.

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i/j:6.2f}", end=" ")
    print() 