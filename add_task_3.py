# Posortuj listę imion = \["Katarzyna", "Jan", "Anna", "Aleksander"\] od najkrótszego do
# najdłuższego, używając sorted() z key=lambda.

name = ["Katarzyna", "Jan", "Anna", "Aleksander"]

sorted_name = sorted(name, key = lambda x: len(x))

print(sorted_name)
