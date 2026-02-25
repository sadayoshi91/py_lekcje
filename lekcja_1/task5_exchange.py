kurs_dolar = 4.0  # Przykładowy kurs wymiany
kwota_zl = float(input("Podaj kwotę w złotych: "))      
kwota_usd = kwota_zl / kurs_dolar

print(f"Kwota w dolarach wynosi: {kwota_usd:.2f} USD")