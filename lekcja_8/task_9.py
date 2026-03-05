# Kontekstowy menedżer with : Pokaż, jak instrukcja with open(...) as f: upraszcza
# kod z zadania 3, eliminując potrzebę jawnego używania bloku finally do zamykania
# pliku

with open("lekcja_8/data_task_9.py") as file:
    # read - czytanie całej zawartości pliku
    file_data = file.read()
    print(file_data)
    # readlines - zwraca kolejne linie pliku jako listę
    file_data = file.readlines()
    print(file_data)
    
with open("lekcja_8/data_task_9.py", mode="a") as file_2:
    my_name = "Jan Kowalski"
    # write - zapis do pliku
    file_2.write(my_name)
