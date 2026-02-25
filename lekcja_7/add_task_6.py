# Użyj reduce(), aby obliczyć sumę kwadratów liczb z listy \[1, 2, 3, 4\]. Wynik: 1 + 4 + 9 + 16 =
# 30.
from functools import reduce

my_list = [1, 2, 3, 4]

new_list = reduce(lambda acc, x: acc + x**2, my_list, 0)

print(new_list)