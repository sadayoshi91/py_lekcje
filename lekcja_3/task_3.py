#analiza stringa: Utwórz zmienną z łańcuchem znaków " Python jest super! " .
#wykonaj następujące działania i wyświetl wynik każdego kroku:
#Usuń zędne białe znaki na początku i na końcu.
#Przekształć cały ciąg na małe litery.
#Zamień słowo "super" na "świetny".
#Wyświetl na ekranie znak pod indeksem 4 .

chain_type = " Python jest super! "
white_text = chain_type.strip() 

print(white_text)
print(white_text.lower())
print(white_text.replace("super", "świetny"))
print(white_text[4])
