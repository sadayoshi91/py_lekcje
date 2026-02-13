# Rozszerz grę z zadania 6: jeśli strzał za mały — "Za mało!", za duży — "Za dużo!". Dodaj licznik
# prób i wyświetl go po odgadnięciu.
# Wskazówka: Zmienna proby = 0 przed pętlą. W pętli: proby += 1. Użyj if/elif/else zamiast if/else.


# zadanie 6
secret = 42 

print("Zgadnij liczbę!")

attempt = 0
while True: 
    number = int(input("Podaj liczbę: "))
    attempt += 1

    if number > secret:
        print("Za dużo!")
    elif number < secret:
        print("Za mało!")
    elif number == secret:
        print("Gratulacje! Trafiłeś poprawną liczbę!")
        break # zakończenie pętli

print(f"Twoja liczba podejść to {attempt}")