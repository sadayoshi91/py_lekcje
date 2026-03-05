# Bezpieczny dostęp do listy
# Napisz funkcję pobierz_element(lista, indeks) zwracającą element o podanym indeksie. Jeśli
# indeks jest poza zakresem, zwróć None. Użyj try/except IndexError.
# Wskazówka: try: return lista\[indeks\] / except IndexError: return None.

def get_element(list_1, index_1):
    try:
        return list_1[index_1]
    except IndexError:
        return None
    
my_list = [10, 20, 30]
print(get_element(my_list, 1))  # Zwraca 20
print(get_element(my_list, 5))  # Zwraca None
