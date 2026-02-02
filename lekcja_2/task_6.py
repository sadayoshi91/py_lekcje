#pytam czy ma prawo jazdy (tak/nie) i ile ma lat. Jeśli ktoś ma 18 lat lub więcej i ma prawo jazdy to wyświetlam True, w przeciwnym razie False
age = int(input("Ile masz lat? "))
has_license = input("Czy masz prawo jazdy? (tak/nie) ").lower() #lower dla pewności że niezależnie czy wpisze TAK Tak tAk itp. to i tak będzie "tak"

if age >= 18 and has_license == "tak":
    print(True)
else:
    print(False)