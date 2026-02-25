# Mini-projekt: Prosty kalkulator walut:
# Zdefiniuj kursy w słowniku, np. kursy = {"USD": 4.0, "EUR": 4.3} .
# W pętli while True zapytaj użytkownika o kwotę w PLN i walutę (USD/EUR).
# Użyj if-elif-else , aby sprawdzić wybraną walutę i obliczyć wynik.
# Sformatuj wynik do dwóch miejsc po przecinku, używając f-stringa.
# Zapytaj użytkownika, czy chce kontynuować. Jeśli odpowie "nie", użyj break 

rate = {
    "USD": 4.0,
    "EUR": 4.3
}

while True: 
    value_pln = float(input("Podaj kwotę w PLN: "))
    currency = input("Wybierz walutę (USD/EUR): ").upper()
# użyć .2f
    if currency == "USD":
        result = value_pln / rate["USD"]
        print(f"Otrzymasz {result:.2f} USD") # użyłem :.2f aby podawało kwotę do 2 miejsc po przecinku
    elif currency == "EUR":
        result = value_pln / rate["EUR"]
        print(f"Otrzymasz {result:.2f} EUR")
    else: 
        print("Nieobsługiwana waluta")
# program ma zapytać czy kontynuujemy
    next = input("Czy chcesz kontynuować? (TAK/NIE): ").lower()
    if next == "nie":
        print("Koniec programu")
        break #zatrzymanie pętli