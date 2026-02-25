#Mini-kalkulator: Napisz program, który prosi użytkownika o podanie dwóch liczb, a
#następnie wyświetla wynik ich dodawania, odejmowania, mnożenia i dzielenia. Pamiętaj o
#konwersji typów z input() .

#Pobieranie danych od użytkownika (jako liczby zmiennoprzecinkowe) 
num_1 = input("Podaj pierwszą liczbę: ")
num_2 = input("Podaj drugą liczbę: ")

#konwersja
num_1_float = float(num_1)
num_2_float = float(num_2)

sum = num_1_float + num_2_float
sub = num_1_float - num_2_float
split = num_1_float / num_2_float
div = num_1_float * num_2_float

print(f"Wynik dodawania: {sum}")
print(f"Wynik odejmowania: {sub}")
print(f"Wynik dzielenia: {split}")
print(f"Wynik mnożenia: {div}")
