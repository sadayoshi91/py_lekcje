# Napisz funkcję sprawdz_email(email: str) -> bool, która zwraca True jeśli email zawiera
# dokładnie jeden znak "@" i co najmniej jedną kropkę po "@". Dodaj docstring.
# Wskazówka: Sprawdź email.count("@") == 1. Podziel przez "@" (split) i sprawdź czy po prawej
# jest kropka.

def check_email(email: str) -> bool:
    """
    Sprawdza, czy email zawiera dokładnie jeden znak '@'
    oraz czy po znaku '@' znajduje się co najmniej jedna kropka.
    Zwraca True lub False.
    """
    if email.count("@") != 1:
        return False

    local_part, domain_part = email.split("@")
    
    if "." in domain_part:
        return True
    
    return False

print(check_email("jan.kowalski@gmail.com"))   # True
print(check_email("jan@gmail"))                # False
print(check_email("jan@@gmail.com"))           # False
print(check_email("jangmail.com"))             # False