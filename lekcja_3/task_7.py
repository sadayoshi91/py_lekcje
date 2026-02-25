#Niemutowalność krotki:
#Utwórz krotkę punkt = (10, 20, 30) .
#Spróbuj zmienić pierwszy element krotki на 15 .
#Wyjaśnij w komentarzu do kodu, dlaczego wystąpił błąd

point = (10, 20, 30)    
#point[0] = 15  #To spowoduje błąd TypeError, ponieważ krotki są niemutowalne i nie można zmieniać ich elementów po utworzeniu  
#W związku z tym próba przypisania nowej wartości do elementu krotki powoduje błąd 
print("Krotki są niemutowalne, więc nie można zmienić ich elementów po utworzeniu.")
