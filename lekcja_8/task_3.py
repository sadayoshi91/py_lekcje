file = open("lekcja_8/data.txt")

# read - czytanie całej zawartości pliku
file_data = file.read()
print(file_data)

# readlines - zwraca kolejne linie pliku jako listę
file_data = file.readlines()
print(file_data)

# mode - r - odczyt, w- zapis (nadpisuje pliku) a - zapis (dodaje dane do pliku)
file_2 = open("lekcja_8/data.txt",
              mode="a")

my_name = "Jan Kowalski"

# write - zapis do pliku
file_2.write(my_name)

# zamykanie plików
file.close()
file_2.close()