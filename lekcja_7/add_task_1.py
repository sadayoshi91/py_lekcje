# Użyj list comprehension, aby z listy range(1, 21) wybrać tylko nieparzyste i podnieść je do
# kwadratu. Wynik: \[1, 9, 25, 49, 81, ...\].

print([x**2 for x in range(1, 21) if x % 2 !=0]) 