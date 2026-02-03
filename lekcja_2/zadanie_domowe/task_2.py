#Zadanie 2.
#Zdefiniuj zmienną to_compare = 10. Następnie za pomocą funkcji input pobierz od użytkownika liczbę (pamiętaj o konwersji) i przypisz ją do zmiennej number.
#Za pomocą instrukcji if sprawdź czy liczba podana przez użytkownika jest większa od zmiennej to_compare, jeżeli tak, wypisz na ekranie komunikat "Większa".

to_compare = 10
number = int(input("Podaj liczbę: ")) #pobieram liczbę i konwertuję ją na int
if number > to_compare: #sprawdzam czy liczba jest większa od to_compare
    print("Większa") #jeśli tak, wypisuję komunikat 
