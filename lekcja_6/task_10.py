# Mini-projekt: Walidator hasła: Stwórz funkcję sprawdz_haslo(haslo: str) -> bool .
# Funkcja powinna sprawdzać, czy hasło spełnia następujące warunki i zwracać True lub
# False :
# Ma co najmniej 8 znaków.
# Zawiera co najmniej jedną wielką literę.
# Zawiera co najmniej jedną cyfrę. Napisz do niej pełną dokumentację (docstring i
# adnotacje).

def check_password(password: str) -> bool:
    if len(password) < 8:
        return False

    capital_letter = False
    have_number = False

    for sign in password:
        if sign.isupper():
            capital_letter = True
        if sign.isdigit():
            have_number = True

    return capital_letter and have_number