#Zadanie 3
#Poproś użytkownika o podanie trzech nazw przedmiotów szkolnych (każdy osobno).
#Program powinien:
#1. Zapisać je do listy.
#2. Zamienić wszystkie nazwy na małe litery.
#3. Sprawdzić, czy lista zawiera "matematyka" lub "informatyka".
#4. Wyświetlić odpowiedni komunikat.

#input z nazwami przedmiotów szkolnych
school_subjects_1 = input("Podaj przedmiot szkolny nr.1: ")
school_subjects_2 = input("Podaj przedmiot szkolny nr.2: ")
school_subjects_3 = input("Podaj przedmiot szkolny nr.3: ")
#zapisanie przedmiotów szkolnych na listę
subjects_list = [school_subjects_1, 
                 school_subjects_2, 
                 school_subjects_3]
print("Przedmioty pomyślnie dodane do listy")
#zamienić wszystkie nazwy na małe litery
small_letters = [subject.lower() for subject in subjects_list]
#sprwadzanie czy znajdują się odpowiednie słowa
check_subjects = "matematyka" in small_letters or "informatyka" in small_letters
if check_subjects:
    print(f"Twoje szkolne przedmioty to: {school_subjects_1}, {school_subjects_2}, {school_subjects_3} (zawiera matematykę kub informatykę)")
else:
    print(f"Twoje szkolne przedmioty to: {school_subjects_1}, {school_subjects_2}, {school_subjects_3} (nie zawiera matematyki lub informatyki)")


