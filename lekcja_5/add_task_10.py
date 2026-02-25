# Program pyta o zdanie. Zlicza i wyświetla:
# liczbę samogłosek
# liczbę spółgłosek (liter niebędących samogłoskami ani spacjami)
# liczbę spacji
# liczbę cyfr
# Użyj pętli for po znakach zdania i if/elif/else do klasyfikacji każdego znaku.

sentence = input("Podaj dowolne zdanie: ")

# samogłoski
vowels = "aeiouyąęóAEIOUYĄĘÓ"
# spółgłoski
consonants = "bcćdfghjklłmnńprsśtwyzźżBCĆDFGHJKLŁMNŃPRSŚTWYZŹŻ"
# spacje
space = " "
# liczby
numbers = "0123456789"
# od siebie dodam jeszcze znaki specjalne z zakresu numerycznego (SHIFT + 1, 2 etc.)
special = "!@#$%^&*()_+-="

vowel_count = 0
consonant_count = 0
space_count = 0
number_count = 0
special_count = 0

for i in sentence:
    if i in vowels:
        vowel_count += 1
    elif i in consonants:
        consonant_count += 1
    elif i in space:
        space_count += 1
    elif i in numbers:
        number_count += 1
    elif i in special:
        special_count += 1

print(f"Samogłoski: {vowel_count}\n"
      f"Spółgłoski: {consonant_count}\n"
      f"Spacje: {space_count}\n"
      f"Cyfry: {number_count}\n"
      f"Znaki Specjalne: {special_count}")

        
