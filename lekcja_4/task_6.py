#Prawda czy fałsz?: Napisz program, który prosi użytkownika o wpisanie dowolnego tekstu.
#Następnie, używając konwersji na bool , sprawdź, czy wpisany tekst jest "prawdziwy"
#(niepusty) i wyświetl odpowiedni komunikat.

text = input("Wprowadź dowolny tekst: ")

if text:
    print("Tekst nie jest pusty")
else: 
    print("Tekst jest pusty")