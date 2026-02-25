# Masz listę produktów:
# produkty = [
# {"nazwa": "laptop", "cena": 3500, "kategoria": "elektronika"},
# {"nazwa": "koszulka", "cena": 59, "kategoria": "odziez"},
# {"nazwa": "słuchawki", "cena": 299, "kategoria": "elektronika"},
# {"nazwa": "spodnie", "cena": 149, "kategoria": "odziez"},
# {"nazwa": "tablet", "cena": 1800, "kategoria": "elektronika"}
# ]
# Napisz jednolinijkowy kod, który:
# Wybiera tylko produkty z kategorii "elektronika"
# Sortuje je po cenie rosnąco
# Zwraca listę nazw (stringów) wielką literą
# Oczekiwany wynik: \["SLUCHAWKI", "TABLET", "LAPTOP"\]
# Wskazówka: Połącz sorted() z key, list comprehension lub filter+map, i .upper(). Można to zrobić
# w jednej linii: \[p\["nazwa"\].upper() for p in sorted(filter(...), key=...)\]

produkty = [
{"nazwa": "laptop", "cena": 3500, "kategoria": "elektronika"},
{"nazwa": "koszulka", "cena": 59, "kategoria": "odziez"},
{"nazwa": "słuchawki", "cena": 299, "kategoria": "elektronika"},
{"nazwa": "spodnie", "cena": 149, "kategoria": "odziez"},
{"nazwa": "tablet", "cena": 1800, "kategoria": "elektronika"}
]

print([p["nazwa"].upper() for p in sorted(filter(lambda p: p["kategoria"] == "elektronika", produkty), key=lambda p: p["cena"])])


