# Napisz dwie funkcje: celsius_na_fahrenheit(c) i fahrenheit_na_celsius(f). Wzory: F = C * 9/5 + 32
# i C = (F - 32) * 5/9. Przetestuj obie.
# Wskazówka: Każda funkcja to jedno obliczenie i return.

# funkcja na separator między funkcjami 
def separator():
    print("-" * 57)
# wersja 1
def celsius_to_fahrenheit(c_v1: float) -> float:
    return c_v1 * 9/5 + 32

def fahrenheit_to_celsius(f_v1: float) -> float:
    return (f_v1 - 32) * 5/9

print(f"V1 Temperatura Fahrenheita wynosi: {celsius_to_fahrenheit(26)}")
print(f"V1 Temperatura Celsjusza wynosi: {fahrenheit_to_celsius(78.8)}")

separator()
# wersja 2

def celsius_to_fahrenheit_v2(c_v2: float) -> float:
    result_c = c_v2 * 9/5 + 32
    return result_c

def fahrenheit_to_celsius_v2(f_v2: float) -> float:
    result_f = (f_v2 - 32) * 5/9
    return result_f

print(f"V2 Temperatura Fahrenheita wynosi: {celsius_to_fahrenheit_v2(32)}")
print(f"V2 Temperatura Celsiusza wynosi: {fahrenheit_to_celsius_v2(91.2)}")

separator()
# wersja 3 z inputem poza funkcją
temp_input_c = float(input("Wprowadź temperaturę w Celsiuszach: "))
temp_input_f = float(input("Wprowadź temperaturę w Fahrenheitach: "))

def celsius_to_fahrenheit_v3(c_v3: float) -> float:
    return c_v3 * 9/5 + 32

def fahrenheit_to_celsius_v3(f_v3: float) -> float:
    return (f_v3 - 32) * 5/9


result_v3_c = celsius_to_fahrenheit_v3(temp_input_c)
print(f"V3 Temperatura w Fahrenheitach wynosi: {result_v3_c}")

result_v3_f = fahrenheit_to_celsius_v3(temp_input_f)
print(f"V3 Temperatura w Celsiuszach wynosi: {result_v3_f}")

separator()
# wersja 4 z global

# zmienne globalne
c_temp = 0.0
f_temp = 0.0

def celsius_to_fahrenheit_global():
    global c_temp
    return c_temp * 9/5 + 32

def fahrenheit_to_celsius_global():
    global f_temp
    return (f_temp - 32) * 5/9


# ustawiamy wartości globalne
c_temp = 26
f_temp = 78.8

print(f"V4 Temperatura w Fahrenheitach wynosi: {celsius_to_fahrenheit_global()}")
print(f"V4 Temperatura w Celsiuszach wynosi: {fahrenheit_to_celsius_global()}")