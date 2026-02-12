# Kalkulator zniżek: Napisz program, który oblicza cenę biletu. Cena bazowa to 100 PLN.
# Jeśli użytkownik jest studentem ( tak/nie ) LUB ma mniej niż 18 lat, przysługuje mu 50%
# zniżki. Użyj operatorów or i and .

ticket_price = 100
age = int(input("Podaj wiek: "))
check_status = str(input("Czy jesteś studentem (TAK/NIE)?: ")).lower()
#sprawdzanie wieku oraz statusu czy jest studentem
if (check_status == "tak" or age < 18) and age >= 0:
    end_price = ticket_price * 0.5
else:
    end_price = ticket_price

print(f"Cena biletu to: {end_price}")


          