# apisz kalkulator jako zestaw funkcji:
# dodaj(a, b), odejmij(a, b), pomnoz(a, b), podziel(a, b)
# wykonaj(a, b, op) — wywołuje odpowiednią funkcję na podstawie operacji
# W pętli while True: pobieraj dane, wykonuj operacje, wyświetlaj wyniki. Dodaj adnotacje typów i
# docstringi do wszystkich funkcji.
# Wskazówka: W wykonaj() użyj if/elif/else aby wywołać właściwą funkcję.

def sum_calc(a: float, b: float) -> float:
    """Zwraca sumę dwóch liczb."""
    return a + b

def sub_calc(a: float, b: float) -> float:
    """Zwraca różnicę dwóch liczb."""
    return a - b

def multi_calc(a: float, b: float) -> float:
    """Zwraca iloczyn dwóch liczb."""
    return a * b

def div_calc(a: float, b: float) -> float | None:
    """Zwraca iloraz dwóch liczb. Jeśli b == 0, zwraca None."""
    if b == 0:
        return None
    return a / b

def operation(a: float, b: float, op: str) -> float | None:
    """Wykonuje działanie matematyczne na podstawie operatora."""
    if op == "+":
        return sum_calc(a, b)
    elif op == "-":
        return sub_calc(a, b)
    elif op == "*":
        return multi_calc(a, b)
    elif op == "/":
        return div_calc(a, b)
    else:
        return None

# pętla programu
while True:
    print("\n--- Kalkulator ---")
    print("Wpisz 'q' aby zakończyć")

    first_number = input("Podaj pierwszą liczbę: ")
    if first_number == "q":
        break

    operator = input("Podaj operator (+, -, *, /): ")
    if operator == "q":
        break

    second_number = input("Podaj drugą liczbę: ")
    if second_number == "q":
        break

    a = float(first_number)
    b = float(second_number)

    result = operation(a, b, operator)

    if result is None:
        print("Błąd: niepoprawna operacja lub dzielenie przez zero.")
    else:
        print("Wynik:", result)