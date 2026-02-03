#Zadanie 4.
#Zdefiniuj dwie zmienne:
#age – wiek użytkownika (pobrany przez input, pamiętaj o konwersji),
#has_ticket – informacja czy użytkownik ma bilet (True albo False – przypisz na sztywno).
#Za pomocą instrukcji if sprawdź:
#jeżeli użytkownik ma co najmniej 18 lat i ma bilet – wypisz "Możesz wejść na koncert"
#w przeciwnym wypadku wypisz "Nie możesz wejść na koncert"

age = int(input("Podaj swój wiek: "))   
has_ticket = True 
if age >= 18 and has_ticket:
    print("Możesz wejść na koncert")
else:
    print("Nie możesz wejść na koncert")