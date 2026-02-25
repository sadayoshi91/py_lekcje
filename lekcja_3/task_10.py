#Mini-projekt "Formater danych": Napisz program, który poprosi użytkownika o jego imię i
#nazwisko w jednej linii (np. " jan kowalski "). Program powinien:
#Oczyścić zbędne białe znaki.
#Sprawić, aby każde słowo zaczynało się wielką literą (metoda .title() ).
#Wyświetlić sformatowane dane oraz ich długość.

full_name = input("Podaj swoje imię i nazwisko: ")  #pobieram imię i nazwisko od użytkownika
cleaned_name = full_name.strip()  #usuwam zbędne białe znaki z początku i końca
formatted_name = cleaned_name.title()  #formatowanie: każde słowo zaczyna się wielką literą
name_length = len(formatted_name)  #obliczam długość sformatowanego łańcucha    

print(f"Sformatowane imię i nazwisko: {formatted_name}")
print(f"Długość sformatowanego łańcucha: {name_length} znaków")

