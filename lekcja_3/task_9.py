#Bramki logiczne: Napisz program, który poprosi o dwie wartości logiczne ( True lub
#False ). Niech użytkownik wprowadza 1 dla True i 0 dla False . Program powinien
#wyświetlić wyniki operacji AND oraz OR dla tych dwóch wartości.

value1 = bool(int(input("Podaj pierwszą wartość logiczną (1 dla True, 0 dla False): ")))
value2 = bool(int(input("Podaj drugą wartość logiczną (1 dla True, 0 dla False): ")))

and_result = value1 and value2
or_result = value1 or value2

print(f"Wynik operacji AND: {and_result}")
print(f"Wynik operacji OR: {or_result}")

