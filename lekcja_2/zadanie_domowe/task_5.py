
#Zadanie 5.
#Pobierz od użytkownika dwie liczby i zapisz je w zmiennych number_1 oraz number_2.
#Za pomocą instrukcji if sprawdź:
#jeżeli którakolwiek z liczb jest równa 0 – wypisz "Jedna z liczb to zero"
#w przeciwnym wypadku wypisz "Żadna z liczb nie jest zerem"

number_1 = int(input("Podaj pierwszą liczbę: "))
number_2 = int(input("Podaj drugą liczbę: "))   

if number_1 == 0 or number_2 == 0:
    print("Jedna z liczb to zero")
else:
    print("Żadna z liczb nie jest zerem")   
