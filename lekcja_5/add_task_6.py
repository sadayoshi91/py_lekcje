# Użytkownik wpisuje produkty w pętli while True. Wpisanie "koniec" kończy wprowadzanie.
# Program przechowuje produkty w liście i na koniec wyświetla je ponumerowane (enumerate z
# start=1).
# Wskazówka: Pusta lista przed pętlą. W pętli: input, sprawdzenie "koniec", append. Po pętli:
# enumerate.

shopping_list = []

while True:
    product = input("Wpisz produkt na listę zakupów (aby zakończyć wpisz KONIEC): ")
    shopping_list.append(product)

    if product.lower() == "koniec":
        break
# printa daję przed pętlą for aby wyświetłało się tylko raz
print ("Twoja lista zakupów prezentuje się następująco:")

for index, shopping_list in enumerate(shopping_list, start=1):
    print (index, ":",shopping_list)