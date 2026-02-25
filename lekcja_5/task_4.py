# Literowanie słowa: Poproś użytkownika o podanie słowa. Użyj pętli for , aby wyświetlić
# każdą literę tego słowa w osobnej linii, poprzedzoną jej indeksem. Przykład dla "Kot": 0:
# K , 1: o , 2: t .

# pobranie słowa od użytkownika
word = input("Podaj słowo: ")

# wyświetlenie każdej litery z jej indeksem
for index, word in enumerate(word):
    print(f"{index}: {word}", end=", ")