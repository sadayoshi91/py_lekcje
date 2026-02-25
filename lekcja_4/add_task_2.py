#Program pyta o liczbę kilometrów. Wyświetla wynik w metrach, centymetrach i milimetrach.
#Wskazówka: 1 km = 1000 m = 100000 cm = 1000000 mm. Użyj float(input(...)) i f-stringów

km = float(input("Podaj liczbę km: "))

print (f"Podana wartość w metrach: {km * 1000}")
print (f"Podana wartość w centymetrach: {km * 100000}")
print (f"Podana wartość w milimetrach: {round((km * 1000000), 2)}")
