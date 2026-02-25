# Mając listę liczb \[1, 5, 12, 7, 20, 3, 18\], użyj filter() z lambda, aby wybrać tylko liczby parzyste
# większe od 10. Wynik: \[12, 20, 18\].

my_list = [1, 5, 12, 7, 20, 3, 18]

filtered_list = list(filter(lambda x: x % 2 == 0 and x > 10, my_list))

print(filtered_list)