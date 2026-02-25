# Napisz funkcję suma_do(n) obliczającą sumę liczb od 1 do n rekurencyjnie. Przypadek bazowy: n
# == 1 daje 1. Krok: n + suma_do(n - 1).
# Wskazówka: Analogicznie do silni, ale zamiast mnożenia jest dodawanie.

def sum_to(n: int) -> int:
    if n == 1:
        return 1 
    else: 
        return n + sum_to(n - 1)
    
print(f"Wynik: {sum_to(5)}")