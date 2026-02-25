# Stwórz domknięcie (closure). Napisz funkcję stworz_licznik() , która
# zwraca funkcję. Każde wywołanie zwróconej funkcji powinno zwiększać wewnętrzny licznik i
# zwracać jego aktualną wartość.

def create_counter():
    counter = 0  # zmienna zewnętrzna (będzie zapamiętana przez closure)

    def counter_func():
        nonlocal counter  # odwołujemy się do zmiennej z zakresu funkcji create_counter
        counter += 1
        return counter

    return counter_func  # zwracamy funkcję -> powstaje closure