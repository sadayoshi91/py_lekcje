# Adnotacje i docstring: Weź funkcję kalkulator z zadania 1. Dodaj do niej pełne
# adnotacje typów dla wszystkich parametrów i wartości zwracanej. Napisz również
# kompletny docstring opisujący jej działanie.

def calcutale(x: float, y: float, operation: str) -> float | None:
    """
    Wykonuje podstawowe operacje arytmetyczne na dwóch liczbach.

    Argumenty:
    x: Pierwszy operand (float)
    y: Drugi operand (float)
    operacja: Operacja do wykonania („+”, „-”, „*”, „/”)

    Zwraca:
    Wynik operacji w postaci liczby zmiennoprzecinkowej lub wartość None, jeśli operacja jest nieprawidłowa lub dzielenie przez zero
    """
    if operation == "+":
        return x + y
    elif operation == "-":
        return x - y
    elif operation == "*":
        return x * y
    elif operation == "/":
        if y == 0:
            return None
        return x / y
    return None

print("+", calcutale(12, 6, "+"))
print("-", calcutale(12, 6, "-"))
print("/ z 0: ", calcutale(12, 0, "/"))
print("/ z: ", calcutale(12, 3, "/"))