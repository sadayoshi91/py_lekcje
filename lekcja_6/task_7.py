# Zwracanie wielu wartości: Stwórz funkcję analiza_listy(lista: list[int]) , która
# przyjmuje listę liczb i zwraca krotkę zawierającą trzy wartości: minimum, maksimum i sumę
# elementów z listy

def list_analysis(list_1: list[int]) -> tuple[int, int, int]:
    # do obsługi jeżeli lista byłaby pusta zwróci True albo False
    if not list_1:
        return (0, 0, 0)
    
    minimum = min(list_1)
    maximum = max(list_1)
    sum_values = sum(list_1)
    
    return (minimum, maximum, sum_values)

