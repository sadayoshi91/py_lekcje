a = float(input("Podaj pierwszą liczbę: "))
znak = input("Podaj działanie (+, -, *, /): ")
b = float(input("Podaj drugą liczbę: "))

if znak == "+":
    wynik = a + b
    print("Wynik:", wynik)

elif znak == "-":
    wynik = a - b
    print("Wynik:", wynik)

elif znak == "*":
    wynik = a * b
    print("Wynik:", wynik)

elif znak == "/":
    if b == 0:
        print("Nie można dzielić przez zero!")
    else:
        wynik = a / b
        print("Wynik:", wynik)

else:
    print("Nieznane działanie!")