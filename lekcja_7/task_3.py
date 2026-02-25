# Użyj funkcji map() , aby przekształcić listę imion imiona =
# ["anna", "piotr", "kasia"] w listę imion pisanych wielką literą.

imiona = ["anna", "piotr", "kasia"]

imiona_map = list(map((lambda i: i.capitalize()), imiona))

print(imiona_map)