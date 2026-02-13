# Program pyta użytkownika o liczby w pętli while. Jeśli użytkownik wpisze 0, pętla się kończy i
# program wyświetla sumę wszystkich wpisanych liczb.
# Wskazówka: Zmienna suma = 0 przed pętlą. W pętli: suma += liczba. Warunek zakończenia: if
# liczba == 0: break.

suma = 0

while True: 
    number = int(input("Podaj liczbę: "))
    if number == 0:
        break

    suma += number 

print(f"Suma liczb wynosi: {suma}")