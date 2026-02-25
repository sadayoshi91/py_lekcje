# Napisz funkcję karta_ucznia(imie, klasa, **oceny) zwracającą słownik. Klucze: "imie", "klasa",
# "oceny" (słownik ocen), "srednia" (średnia z ocen). Np. karta_ucznia("Jan", "3B", matematyka=4,
# fizyka=5).
# Wskazówka: Średnia = sum(oceny.values()) / len(oceny).

def student_card(name, student_class, **grades: int):
    
    return {
    "imie": name,
    "klasa": student_class,
    "oceny": grades,
    "srednia": sum(grades.values()) / len(grades)
}

print(student_card("Piotr", "1B", matematyka=4, fizyka=5))