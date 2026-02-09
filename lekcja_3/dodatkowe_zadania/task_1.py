#Zadanie 1
#Poproś użytkownika o:
#- imię,
#- wiek,
#- wzrost w metrach.
#Program powinien:
#1. Sprawdzić, czy imię po usunięciu spacji nie jest puste.
#2. Sprawdzić, czy wiek jest większy od 0.
#3. Sprawdzić, czy wzrost mieści się w przedziale 1.0 – 2.5.
#Jeżeli wszystkie warunki są spełnione, wyświetl:
#Dane poprawne
#W przeciwnym wypadku:
#Błędne dane

name = input("Podaj swoje imię: ")  
age = input("Podaj swój wiek: ")
height = input("Podaj swój wzrost (w metrach): ")

if name.strip() == "":
    print("Błędne dane")
else:
    age_int = int(age)
    height_float = float(height)

    if age_int > 0 and 1.0 <= height_float <= 2.5:
        print("Dane poprawne")
    else: 
        print("Dane błędne")
