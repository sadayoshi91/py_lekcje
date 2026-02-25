#Rzutowanie typów: Utwórz zmienną liczba_str = "5.8" . Przekonwertuj ją najpierw na
#float , a następnie na int i wyświetl wyniki obu konwersji. Co zauważyłeś podczas
#konwersji float na int ?

number_str = "5.8"
number_float = float(number_str)  #konwertuję na float
number_int = int(number_float)  #konwertuję na int
print("Float:", number_float)
print("Int:", number_int)
# Podczas konwersji float na int część ułamkowa zostaje odcięta a nie zaokrąglona 