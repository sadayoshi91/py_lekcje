# Użyj funkcji filter() , aby z listy liczb od 1 do 30 wybrać
# tylko liczby pierwsze. (Wskazówka: napisz pomocniczą funkcję czy_pierwsza(n) , która
# sprawdza, czy liczba jest pierwsza).

def czy_pierwsza(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numbers = [i for i in range(1, 31)]

filtered_numbers = list(filter(czy_pierwsza, numbers))

print(f"Liczy pierwsze: {filtered_numbers}")