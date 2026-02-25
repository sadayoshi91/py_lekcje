# Napisz funkcję buduj_zdanie(*slowa, separator=" ") zwracającą string ze wszystkich słów
# połączonych separatorem. Np. buduj_zdanie("Ala", "ma", "kota") daje "Ala ma kota".
# Wskazówka: Użyj separator.join(slowa).

def build_sentence(*words, separator=" "):
    return separator.join(words)

print(build_sentence("Ala", "ma", "kota"))
print(build_sentence("Python", "jest", "super"))
