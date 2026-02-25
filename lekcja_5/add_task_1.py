# Ćwiczenie S1: Klasyfikator ocen
# Program pyta o ocenę (1-6). Wyświetla słownie: 6 = "celujący", 5 = "bardzo dobry", 4 = "dobry",
# 3 = "dostateczny", 2 = "dopuszczający", 1 = "niedostateczny". Dla innych wartości:
# "Nieprawidłowa ocena".
# Wskazówka: Użyj if/elif/elif/.../else.

oceny_lista = {6: "celujący", 5: "bardzo dobry", 4: "dobry", 3: "dostateczny", 2: "dopuszczający", 1: "niedostateczny"}

ocena = int(input("Podaj ocenę od 1 do 6: "))

print(oceny_lista.get(ocena, "Nieprawidłowa ocena"))
