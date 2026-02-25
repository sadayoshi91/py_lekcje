#Zadanie 5
#Poproś użytkownika o:
#- imię i nazwisko w jednej linii,
#- rok urodzenia.
#Program powinien:
#1. Poprawnie sformatować imię i nazwisko.
#2. Obliczyć wiek użytkownika.
#3. Wyświetlić inicjały użytkownika (np. J.K).
#4. Wyświetlić informację, czy użytkownik jest pełnoletni.

#zmienne
name_subname = input("Podaj imię i nazwisko (w jednej lini): ")
year_birth = input("Podaj rok urodzenia: ")
#zamiana year_birth na int oraz podzielenie imienia i nazwiska na 2 osobne słowa
year_birth_int = int(year_birth)
data_1 = name_subname.split()
#zapisanie zmiennych + formatowanie
name = data_1[0].capitalize()
subname = data_1[1].capitalize()
#najpierw formatowanie 
name_upper = name_subname.capitalize()
#wiek użytkownika
age_user = 2026 - year_birth_int
print(f"Użytkownik ma {age_user} lat!")   
#inicjały
initials = data_1[0][0].upper() + "." + data_1[1][0].upper() + "."
print(f"Twoje inicjały to: {initials}")
#sprawdzanie pełnoletności użytkownika
if age_user > 18:
    print(f"Użytkownik {name} {subname} jest pełnoletni")
else:
    print(f"Użytkownik {name} {subname} jest niepełnoletni!")
#zakonczenie programu
