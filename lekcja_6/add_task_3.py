# Ćwiczenie S3: Pozdrowienie z domyślnym językiem
# Napisz funkcję pozdrow(imie, jezyk="pl"). Dla "pl" zwraca "Cześć, {imie}!", dla "en" — "Hello,
# {imie}!", dla "de" — "Hallo, {imie}!". Dla nieznanego języka: "Hi, {imie}!".
# Wskazówka: if/elif/else z return dla każdego języka

def greetings(name_1: str, language_1: str = "pl") -> str:
    if language_1 == "pl":
        return f"Cześć, {name_1}!"
    elif language_1 == "en":
        return f"Hello, {name_1}!"
    elif language_1 == "de":
        return f"Hallo, {name_1}!"
    else:
        return f"Hi, {name_1}!"
    
print(greetings("Piotr"))
print(greetings("Piotr", "en"))
print(greetings("Piotr", "de"))
print(greetings("Piotr", "es"))