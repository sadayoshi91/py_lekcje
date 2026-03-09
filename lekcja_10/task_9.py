# Stwórz klasę RejestracjaUzytkownika. W konstruktorze init przyjmuj email i haslo.
# Wewnątrz konstruktora dodaj walidację:
# Sprawdź, czy email zawiera znak @ . Jeśli nie, podnieś wyjątek ValueError z
# odpowiednim komunikatem.
# Sprawdź, czy haslo ma co najmniej 8 znaków. Jeśli nie, podnieś ValueError. Użyj bloku
# try...except, aby przetestować tworzenie obiektów z poprawnymi i niepoprawnymi
# danymi.

# utworzeni klasy RejestracjaUzytkownika z walidacją email i hasła
class UserRegistration:
    def __init__(self, email, password):
        if '@' not in email:
            raise ValueError("Email musi zawierać znak @")
        if len(password) < 8:
            raise ValueError("Hasło musi mieć co najmniej 8 znaków")
        self.email = email
        self.password = password

# testowanie tworzenia obiektów z poprawnymi i niepoprawnymi danymi
try:
    user_1 = UserRegistration("test@example.com", "haslo123")
    print("Użytkownik1 został utworzony pomyślnie.")
except ValueError as e:
    print(f"Błąd przy tworzeniu użytkownika1: {e}")

try:
    user_2 = UserRegistration("testexample.com", "haslo123")
    print("Użytkownik2 został utworzony pomyślnie.")
except ValueError as e:
    print(f"Błąd przy tworzeniu użytkownika2: {e}")

try:
    user_3 = UserRegistration("test@example.com", "haslo")
    print("Użytkownik3 został utworzony pomyślnie.")
except ValueError as e:
    print(f"Błąd przy tworzeniu użytkownika3: {e}")

