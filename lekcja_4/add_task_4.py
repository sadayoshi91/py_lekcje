#Poziom 2: if/elif/else, id(), truthy/falsy
#Ćwiczenie S4: Sprawdzacz temperatury
#Program pyta o temperaturę ciała. Wyświetla:
#poniżej 36.0: "Hipotermia"
#od 36.0 do 37.0: "Norma"
#od 37.1 do 38.0: "Stan podgorączkowy"
#powyżej 38.0: "Gorączka"
#Wskazówka: Użyj if/elif/elif/else z porównaniami.

print("Witamy w internetowym termometrze")
temperature = float(input("Podaj temperaturę ciała: "))

if temperature < 36.0:
    print("Hipotermia")
elif 36.0 <= temperature <= 37.0:
    print("Norma")
elif 37.1 <= temperature <= 38.0:
    print("Stan podgorączkowy")
elif temperature > 38.0:
    print("Gorączka")
else:
    print("Umarłeś")

