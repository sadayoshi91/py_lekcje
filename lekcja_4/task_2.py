#Identyfikator obiektu: Utwórz trzy zmienne ( a , b , c ) z tą samą wartością 256 . Sprawdź
#i wyświetl ich id() . Następnie utwórz trzy zmienne z wartością 257 i również sprawdź ich
#id() . Czy widzisz różnicę w zachowaniu Pythona? Wyjaśnij dlaczego w komentarzu.

a = 256
b = 256
c = 256
a1 = 257
b1 = 257
c1 = 257 

print (id(a))
print (id(b))
print (id(c))
print (id(a1))
print (id(b1))
print (id(c1))

