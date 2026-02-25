#  Wyszukiwarka w liście: Stwórz listę imion: imiona = ["Anna", "Jan", "Piotr",
# "Kasia"] . Poproś użytkownika o podanie imienia do wyszukania. Użyj pętli for z
# instrukcją break oraz blokiem else , aby:
# Jeśli imię zostanie znalezione, wyświetlić "Znaleziono!" i przerwać pętlę.
# Jeśli pętla zakończy się bez znalezienia imienia, wyświetlić "Nie znaleziono imienia na
# liście."

name_list = ["Anna", "Jan", "Piotr", "Kasia"]
name_input = input("Podaj imię do wyszukania: ")

for i in name_list:
    if name_input == i:
        print("Znalezione!")
        break
else:
    print("Nie znaleziono imienia na liście!")