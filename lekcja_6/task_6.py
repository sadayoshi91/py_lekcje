# Wielokrotne powitanie: Napisz funkcję wielokrotne_powitanie(imie: str, ilosc:
# int) -> None , która wyświetla powitanie f"Cześć, {imie}!" tyle razy, ile wynosi
# ilosc . Ta funkcja nie powinna niczego zwracać.

def hello_repeat(name: str, quantity: int) -> None:
    # użyłem podłogi _ - w poleconej książce wyczytałem, że to może byc użyte jako pusta zmienna bądź zmienna która nie będzie używana
    for _ in range(quantity):
        print(f"Cześć, {name}!")