#Zadanie 4
#Poproś użytkownika o:
#- wiek,
#- informację czy ma prawo jazdy (1 – tak, 0 – nie).
#Program powinien:
#- jeżeli wiek < 18 → "Nie możesz prowadzić pojazdu"
#- jeżeli wiek ≥ 18 i brak prawa jazdy → "Musisz zrobić prawo jazdy"
#- jeżeli wiek ≥ 18 i ma prawo jazdy → "Możesz prowadzić pojazd"

#zmienne jako input
age = input("Podaj wiek: ")
driving_license = input("Czy masz prawo jazdy? 1 - tak, 0 - nie: ")
#zmiana na liczby całkowite
age_int = int(age)
driving_license_int = int(driving_license)

#sprawdzanie warunków programu 
if age_int < 18:
    print("Nie możesz prowadzić pojazdu")
elif driving_license_int not in [0, 1]:
    print("Błędne dane - musisz wpisać 0 lub 1")
elif driving_license_int == 0:
    print("Musisz zrobić prawo jazdy!")
else:  
    print("Możesz prowadzić samochód!")
    
