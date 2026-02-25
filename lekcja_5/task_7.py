# Tylko samogłoski: Poproś użytkownika o zdanie. Użyj pętli for oraz instrukcji continue ,
# aby wyświetlić tylko samogłoski z tego zdania. (Wskazówka: if litera not in
# "aeiouy": continue )

# Pobranie zdania od użytkownika
sentence = input("Podaj zdanie: ")

# Zbiór samogłosek (małe i wielkie litery)
vowels = "aeiouyąęóAEIOUYĄĘÓ"

# Przechodzimy po każdej literze
for letter in sentence:
    if letter not in vowels:
        continue  # pomiń znak, jeśli nie jest samogłoską
    print(letter, end=" ")