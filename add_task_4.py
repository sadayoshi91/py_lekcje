# Mając listę liczb \[1, 2, 3, 4, 5\], stwórz słownik, gdzie kluczem jest liczba, a wartością jej
# sześcian. Wynik: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}.

my_list = [1, 2, 3, 4, 5]

new_list ={x: x**3 for x in [1, 2, 3, 4, 5]}

print(new_list)