# Masz słownik oceny = {"Jan": 4, "Anna": 5, "Piotr": 3,
# "Kasia": 4} . Użyj funkcji sorted() i funkcji lambda, aby posortować elementy
# słownika (klucz, wartość) według ocen (od najwyższej do najniższej).

oceny = {"Jan": 4, "Anna": 5, "Piotr": 3, "Kasia": 4}

print(f"{oceny.items()}")

lista_ocen = sorted(oceny.items(), key = lambda ocena: ocena[1], reverse=True)

print(f"{lista_ocen} {lista_ocen[1]}")