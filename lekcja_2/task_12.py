# walidator hasła
# pobrać hasło od użytkownika
# sprawdzić czy hasło spełnia następujące warunki: dług. min 8 znakow, brak spacji w haśle.
password = input("Podaj hasło: ")   
if len(password) >= 8 and ' ' not in password:
    print(f"Hasło {password} jest poprawne.") #wyświetlamy informację czy hasło jest poprawne czy nie
# wyswietlam jaki błąd został popełniony (za krótkie hasło lub spacja w haśle) wykorzystująć dodatkowe ify (nie wiem czy to jest najlepsze rozwiązanie) 
if len(password) < 8:
    print("Błąd: Hasło jest za krótkie.")   
if ' ' in password:
    print("Błąd: Hasło zawiera spację.")