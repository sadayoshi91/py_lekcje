#  Gra "Zgadnij liczbę":
# Program "myśli" o liczbie (np. sekret = 42 ).
# Użyj pętli while True , aby w nieskończoność prosić użytkownika o podanie liczby.
# Wewnątrz pętli, sprawdź, czy podana liczba jest równa sekretnej. Jeśli tak, wyświetl
# gratulacje i użyj break , aby zakończyć grę. Jeśli nie, poinformuj, że to zła liczba.

secret = 42 

print("Zgadnij liczbę!")

while True: 
    number = int(input("Podaj liczbę: "))

    if number == secret:
        print("Gratulacje, zgadłeś liczbę!")
        break # zakończenie pętli 
    else:
        print("Niestety to jest zła liczba") 