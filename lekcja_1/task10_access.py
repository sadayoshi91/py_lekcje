
#zasada - wpuszczane są dzieci o wzroście od 120 cm "I" z osobą dorosłą, "LUB" młodzież o wzroście od 160cm. 
#zapytać o wzrost i czy jest opiekun (tak/nie)
#używając and i or określ czy można wpuścić gościa i wyświetl True lub False
wzrost = int(input("Podaj swój wzrost w cm: "))
opiekun = input("Czy masz opiekuna? (tak/nie): ").lower()
if (wzrost >= 120 and opiekun == "tak") or (wzrost >= 160):
    print(True)
else:
    print(False)
    