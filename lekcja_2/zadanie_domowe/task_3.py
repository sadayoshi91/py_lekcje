#adanie 3.
#Zdefiniuj zmienną current_year i przypisz do niej obecny rok. Pobierz od użytkownika jego rok urodzenia. Oblicz wiek użytkownika, a następnie za pomocą instrukcji if wyświetl odpowiedni komunikat:
#Jeżeli wiek jest mniejszy niż 18 - "Jesteś niepełnoletni"
#Jeżeli wiek jest większy bądz równy 18 ale mniejszy od 65 - "Jesteś dorosły"
#Jeżeli wiek jest większy bądź równy 65 - "Jesteś seniorem"

current_year = 2026
birth_year = int(input("Podaj swój rok urodzenia: "))
age = current_year - birth_year

if age < 18:
    print("Jesteś niepełnoletni")
elif 18 <= age < 65:
    print("Jesteś dorosły")
else:
    print("Jesteś seniorem")   