# Utwórz zmienną x = "globalna" na poziomie modułu. Napisz funkcję, która wewnątrz tworzy
# lokalną x = "lokalna" i wyświetla ją. Po wywołaniu funkcji wyświetl x na zewnątrz. Sprawdź, czy
# globalna x się zmieniła.
# Wskazówka: Nie zmieni się — lokalna zmienna istnieje tylko wewnątrz funkcji.

x = "globalna"

def local_c(x: str) -> str:
    x = "lokalna"
    return x

print(x)