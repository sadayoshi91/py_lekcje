#Komentowanie kodu: Poniżej znajduje się fragment kodu. Dodaj do niego komentarze
#jednoliniowe oraz docstring dla funkcji, wyjaśniając, co robi każda część.
#def oblicz_pole_prostokata(a, b):
# Tutaj dodaj docstring
# Tutaj dodaj komentarz
#pole = a * b
# Tutaj dodaj komentarz
#return pole
#bok_a = 10
#bok_b = 20
#wynik = oblicz_pole_prostokata(bok_a, bok_b)
#print(f"Pole prostokąta o bokach {bok_a} i {bok_b} wynosi {wynik}.")#

def oblicz_pole_prostokata(a, b):
    '''funkcja przyjmuje wartość boków'''
# wzór na pole prostokąta
    pole = a * b
# zwraca wynik
    return pole
bok_a = 10
bok_b = 20
wynik = oblicz_pole_prostokata(bok_a, bok_b)
print(f"Pole prostokąta o bokach {bok_a} i {bok_b} wynosi {wynik}.")