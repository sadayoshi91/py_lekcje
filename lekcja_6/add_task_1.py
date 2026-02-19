# Napisz funkcję pole_trojkata(podstawa, wysokosc) zwracającą pole trójkąta (podstawa *
# wysokosc / 2). Przetestuj z różnymi wartościami.
# Wskazówka: Jeden return z wyrażeniem.

def triangle_area(base: float, height: float) -> float:
    return base * height / 2

print(f"Pole trójkąta wynosi: {triangle_area(2, 5)}")
print(f"Pole trójkąta wynosi: {triangle_area(10, 4)}")
print(f"Pole trójkąta wynosi: {triangle_area(3.5, 2)}")
print(f"Pole trójkąta wynosi: {triangle_area(7, 7)}")