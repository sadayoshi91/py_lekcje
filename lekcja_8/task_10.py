# Mini-projekt: Sumator liczb z pliku: Napisz program, który:
# a. Pyta użytkownika o nazwę pliku.
# b. Otwiera plik i czyta go linia po linii.
# c. Każdą linię próbuje przekonwertować na liczbę i dodać do sumy.
# d. Ignoruje linie, których nie da się przekonwertować na liczbę (obsługa ValueError).
# e. Obsługuje FileNotFoundError, jeśli plik nie istnieje.
# f. Na końcu, w bloku finally, wyświetla obliczoną sumę (nawet jeśli wystąpiły błędy po
# drodze).

def sum_from_file(filename):
    total_sum = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    total_sum += number
                except ValueError:
                    print(f"Nie można przekonwertować '{line.strip()}' na liczbę. Pomijam tę linię.")
    except FileNotFoundError:
        print(f"Plik '{filename}' nie został znaleziony.")
    finally:
        print(f"Suma liczb z pliku: {total_sum}")
filename = input("Podaj nazwę pliku: ")
sum_from_file(filename)
