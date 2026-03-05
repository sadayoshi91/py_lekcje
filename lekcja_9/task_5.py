# Masz listę słowników: produkty = [{"nazwa": "Mleko", "cena":
# 3.50}, {"nazwa": "Chleb", "cena": 4.20}] . Zapisz te dane do pliku produkty.csv ,
# gdzie pierwszy wiersz to nagłówki ("nazwa", "cena").

import csv
produkty = [{"nazwa": "Mleko", "cena": 3.50}, {"nazwa": "Chleb", "cena": 4.20}]

with open("lekcja_9/produkty.csv", mode="w", newline="", encoding="utf-8") as file:
    fieldnames = ["nazwa", "cena"]
    writer = csv.DictWriter(file, fieldnames=fieldnames) # o dictwriter dowiedziałem sie z dokumentacji, jest to klasa, która umożliwia zapis słowników do pliku CSV, gdzie klucze słownika odpowiadają nagłówkom kolumn w pliku CSV
    # Zapisz nagłówki do pliku CSV
    writer.writeheader()

    # Zapisz dane produktów do pliku CSV
    for produkt in produkty:
        writer.writerow(produkt)