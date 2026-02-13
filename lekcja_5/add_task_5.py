# Program pyta o 5 liczb (pętla for z range). Wyświetla tylko te, które są większe od 10. Użyj
# continue aby pominąć resztę.
# Wskazówka: Jeśli liczba <= 10, użyj continue. W przeciwnym razie wyświetl.


for i in range(5):
    # użyłem najpierw zwykłego stringa aby obsłuzyć błąd wciśnięcia entera bez podania cyfry 
    numbers_str = input("Podaj liczbę: ") 
    
    #sprawdzenie zawartości stringa
    if numbers_str == "":
        print("Błąd! Wprowadź liczbę!")
        continue
    #zamiana stringa na int
    numbers_int = int(numbers_str)

    if numbers_int <= 10:
        continue
    
    print(numbers_int)