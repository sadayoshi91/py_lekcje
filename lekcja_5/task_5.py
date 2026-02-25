# Tabela mnożenia: Napisz program, który używając zagnieżdżonych pętli for (jedna w
# drugiej), wyświetli tabliczkę mnożenia od 1 do 5. (Wskazówka: for i in range(1, 6):
# for j in range(1, 6): ... ).

# tabliczka mnożenia
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ") # :3 wyrównuje liczby do szerokości 3 znaków
    print() # przejście do nowej lini po zakończeniu jednego wiersza (print() jest w bolku pętli J)

# do zrobienia kolumny i wiersze 