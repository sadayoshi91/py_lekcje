# Tworzenie profilu: Napisz funkcję stworz_profil(imie, **dane_dodatkowe) , która
# przyjmuje imię oraz dowolną liczbę nazwanych argumentów (np. wiek=30 ,
# miasto="Warszawa" ). Funkcja powinna zwrócić słownik z profilem użytkownika, gdzie
# klucz 'imie' jest obowiązkowy, a reszta danych jest pobierana z **dane_dodatkowe .

def create_profile(name, **add_data):
    profile = {"Imię": name}
    profile.update(add_data)
    return profile

profile_1 = create_profile("Piotr", age=30, city="Warszawa")
profile_2 = create_profile("Anna", second_name="Joanna", hobby="Fotografia")

print(profile_1)
print(profile_2)

