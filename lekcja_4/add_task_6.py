# Program pyta użytkownika o imię, wiek i miasto. Dla każdego pola sprawdza, czy użytkownik
# wpisał coś (bool konwersja). Wyświetla podsumowanie: które pola wypełniono, a które
# zostawiono puste.
# Wskazówka: Pusty input() (użytkownik nacisnął Enter) to "" — a bool("") to False.

name = input("Podaj imię: ")
age = int(input("Podaj wiek: "))
town = input("Podaj miasto: ")

print ("\nPodsumowanie: ")

print ("Imię podane:", bool(name))
print ("Podany wiek:", bool(age))
print ("Podane miast:", bool(town))