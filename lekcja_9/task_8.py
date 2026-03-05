# Wyobraź sobie, że masz duży plik log.txt . Napisz program, który
# pyta użytkownika o szukane słowo (np. "ERROR") i zapisuje wszystkie linie zawierające to
# słowo do nowego pliku wyniki_wyszukiwania.txt .

def search_in_file(search_word, input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                if search_word in line:
                    outfile.write(line)
        print(f"Wszystkie linie zawierające '{search_word}' zostały zapisane do '{output_file}'.")
    except FileNotFoundError:
        print(f"Plik '{input_file}' nie został znaleziony.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
search_word = input("Podaj słowo do wyszukania: ")
input_file = "lekcja_9/log.txt"
output_file = "lekcja_9/wyniki_wyszukiwania.txt"
search_in_file(search_word, input_file, output_file)
