#Zadanie 6.
#Pobierz od użytkownika pierwszy składnik na danie i zapisz go w zmiennej ingredient_1. Następnie pobierz drugi składnik i zapisz go w zmiennej ingredient_2.
#Za pomocą funkcji if napisz program, który spróbuje zgadnąć jakie danie próbuje zrobić użytkownik.
#Wyświetl odpowiedni komunikat:
#Jeżeli użytkownik wybrał jajka i mleko - "Robisz naleśniki"
#Jeżeli użytkownik wybrał jajka i masło - "Robisz jajecznicę"
#Jeżeli jeden ze składników (drugi może być dowolny) to mąka - "Robisz ciasto"
#Jeżeli nie rozpoznajesz żadnego ze składników - "Nie wiem co masz zamiar zrobić"mą

ingredient_1 = input("Podaj pierwszy składnik na danie (jajko/mleko/masło/mąka): ").lower()  #w obu zmiennych .lower() 
ingredient_2 = input("Podaj pierwszy składnik na danie (jajko/mleko/masło/mąka): ").lower() 

#użyłem or zamiast and ponieważ składniki mogą być podane w dowolnej kolejności
if ingredient_1 == "jajko" or ingredient_2 == "mleko": 
    print("Robisz nalesniki")
elif ingredient_1 == "jajko" or ingredient_2 == "masło":
    print("Robisz jajecznicę") 
#użyłem także or ponieważ wystarczy że jeden ze składników to mąka 1 albo 2 
elif ingredient_1 == "mąka" or ingredient_2 == "mąka":
    print("Robisz ciasto")
else:
    print("Nie wiem co masz zamiar zrobić") 