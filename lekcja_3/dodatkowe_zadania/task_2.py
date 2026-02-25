#Zadanie 2
#Poproś użytkownika o podanie zdania.
#Program powinien:
#- usunąć zbędne spacje,
#- sprawdzić długość zdania,
#- sprawdzić, czy zdanie zawiera słowo "python" (bez względu na wielkość liter),
#- wyświetlić długość zdania oraz informację, czy zawiera słowo "python".

sentence = input("Podaj dowolne zdanie które zawiera słowo python: ")
#usuwanie zbędnych spacji za pomocą .join (musiałem znaleźć instukcję .join w internecie)
sentence_clear = " ".join(sentence.split())
#sprawdzanie długości wyczyszczonego zdania ze zbędnych spacji
sentence_length = len(sentence_clear)
#sprwadzanie czy zdanie zawiera słowo python bez względu na wielkośc liter
sentence_word = sentence_clear.lower().split()
sentence_with_word = "python" in sentence_word
#wyświetlanie długości zdania wraz z informacją o słowie
print(f"Długośc zdania: {sentence_length}")
if sentence_with_word:
    print("Zdanie zawiera słowo python")
else:
    print("Zdanie nie zawiera słowa python")
