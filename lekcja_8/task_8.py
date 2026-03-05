# Walidacja hasła v2: Rozbuduj funkcję do walidacji hasła. Powinna ona zwracać listę
# wszystkich błędów walidacji, zamiast rzucać wyjątkiem po pierwszym napotkanym
# problemie. Jeśli lista błędów nie jest pusta, rzuć własnym wyjątkiem BladWalidacjiError ,
# przekazując do niego tę listę.

# użyłem walidatora z lekcji 6

class BladWalidacjiError(Exception):
    def __init__(self, errors):
        self.errors = errors
        super().__init__("Błędy walidacji: " + ", ".join(errors))
    
def check_password(password: str) -> bool:
    errors = []
    if len(password) < 8:
        errors.append("Hasło musi mieć co najmniej 8 znaków")

    capital_letter = False
    have_number = False

    for sign in password:
        if sign.isupper():
            capital_letter = True
        if sign.isdigit():
            have_number = True

    if not capital_letter:
        errors.append("Hasło musi zawierać co najmniej jedną wielką literę")
    if not have_number:
        errors.append("Hasło musi zawierać co najmniej jedną cyfrę")

    if errors:
        raise BladWalidacjiError(errors)

    return True