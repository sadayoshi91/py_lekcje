#  Mini-projekt: Menedżer kontaktów
# Napisz program przechowujący kontakty w słowniku. Funkcje:
# dodaj_kontakt(kontakty, imie, telefon) — dodaje kontakt, raise ValueError jeśli imie jest
# puste
# pobierz_kontakt(kontakty, imie) — zwraca telefon lub raise KeyError
# usun_kontakt(kontakty, imie) — usuwa kontakt lub raise KeyError
# Główna pętla: menu z opcjami (dodaj, pobierz, usuń, wyjdź). Każda operacja w try/except.
# Zapisz kontakty do pliku "kontakty.txt" w finally na końcu programu.
# Wskazówka: Słownik kontakty = {}. W pętli while True: wyświetl menu, pobierz wybór, wywołaj
# odpowiednią funkcję w try/except.

def add_contact(contacts, name, phone):
    if not name:
        raise ValueError("Imię nie może być puste.")
    contacts[name] = phone
    
def get_contact(contacts, name):
    if name not in contacts:
        raise KeyError("Kontakt nie istnieje.")
    return contacts[name]

def delete_contact(contacts, name):
    if name not in contacts:
        raise KeyError("Kontakt nie istnieje.")
    del contacts[name]
def save_contacts(contacts, filename="kontakty.txt"):
    with open(filename, 'w') as file:
        for name, phone in contacts.items():
            file.write(f"{name}:{phone}\n")
contacts = {}
while True:
    print("\nMenedżer Kontaktów")
    print("1. Dodaj kontakt")
    print("2. Pobierz kontakt")
    print("3. Usuń kontakt")
    print("4. Wyjdź")
    
    choice = input("Wybierz opcję (1-4): ")
    
    try:
        if choice == '1':
            name = input("Podaj imię: ")
            phone = input("Podaj numer telefonu: ")
            add_contact(contacts, name, phone)
            print("Kontakt dodany.")
        elif choice == '2':
            name = input("Podaj imię: ")
            phone = get_contact(contacts, name)
            print(f"Numer telefonu dla {name}: {phone}")
        elif choice == '3':
            name = input("Podaj imię: ")
            delete_contact(contacts, name)
            print("Kontakt usunięty.")
        elif choice == '4':
            save_contacts(contacts)
            print("Kontakty zapisane. Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
    except ValueError as ve:
        print(f"Błąd: {ve}")
    except KeyError as ke:
        print(f"Błąd: {ke}")
        