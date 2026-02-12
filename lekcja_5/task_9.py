# Potęgi dwójki: Użyj pętli while i skróconego operatora przypisania *= , aby wyświetlić
# potęgi liczby 2, które są mniejsze niż 1000 (1, 2, 4, 8, ..., 512).

number = 1
print(number)

while True:
    number *= 2
    if number > 1000:
        break
    print(number)