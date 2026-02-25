# Użyj funkcji reduce() , aby obliczyć iloczyn (wynik mnożenia)
# wszystkich liczb w liście [1, 2, 3, 4, 5] 

# z narzedzia functools zaimportowana została funkcja reduce
from functools import reduce
# funkcja do zwracania iloczynu
def dif_num(a, b):
    return a * b

my_list = [1, 2, 3, 4, 5]

print(reduce(dif_num, my_list))


    
