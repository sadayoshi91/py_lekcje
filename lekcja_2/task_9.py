#Wyświetl na ekranie tylko pierwsze dwie linijki z "Zenu Pythona".
#Wskazówka: musisz pobrać cały tekst i przetworzyć go jako ciąg znaków lub listę.
text = """Zen Pythona, autor Tim Peters 
Piękno jest lepsze niż brzydota.
Prostota jest lepsza niż złożoność.
Złożoność jest lepsza niż skomplikowanie.       
Czytelność ma znaczenie.
Specjalne przypadki nie są na tyle specjalne, by łamać zasady.
Chociaż praktyczność zwycięża nad czystością.
Błędy nigdy nie powinny przechodzić cicho.
Chyba że zostały wyraźnie zignorowane.
W obliczu niejednoznaczności, odrzuć pokusę zgadywania.
Powinien istnieć jeden – i najlepiej tylko jeden – oczywisty sposób, by to zrobić.
Chociaż ten sposób może nie być od razu oczywisty, jeśli nie jesteś Holendrem.
Teraz lepiej niż nigdy.
Chociaż nigdy jest często lepsze niż *teraz*.
Jeśli implementacja jest trudna do wyjaśnienia, to jest zła idea.
Jeśli implementacja jest łatwa do wyjaśnienia, to może być dobra idea.
Nazwy przestrzeni są jednym wielkim pomysłem – kontynuujmy ten trend!
W przypadku niejasności, unikaj zgadywania.
Zawsze powinien istnieć jeden – i najlepiej tylko jeden – oczywisty sposób, by to zrobić.
Chociaż ten sposób może nie być od razu oczywisty, jeśli nie jesteś Holendrem.
"""
lines = text.split('\n')
print(lines[0])
print(lines[1])
