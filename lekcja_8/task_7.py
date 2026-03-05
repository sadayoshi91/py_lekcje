# Napisz funkcję pobierz_wartosc(slownik,
# klucz) , która bezpiecznie zwraca wartość dla danego klucza. Jeśli klucza nie ma, funkcja
# nie powinna rzucać błędu, tylko zwracać None . Zrób to bez użycia try...except
# (wskazówka: metoda .get() ). Następnie napisz drugą wersję z użyciem try...except
# KeyError .

def get_value(dict_1, key_1):
    return dict_1.get(key_1)

def get_value_try(dict_1, key_1):
    try:
        return dict_1[key_1]
    except KeyError:
        print("Nie ma takiego klucza")
        return None

dict_2 = {"a": 1, "b": 2, "c": 3}
print(get_value(dict_2, "a"))  # Zwraca 1
print(get_value(dict_2, "d"))  # Zwraca None
print(get_value_try(dict_2, "b"))  # Zwraca 2
print(get_value_try(dict_2, "e"))  # Zwraca None i wypisuje komunikat o braku klucza


