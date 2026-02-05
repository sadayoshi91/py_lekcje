#Tworzenie i typowanie: Utwórz zmienne przechowujące Twoje imię (str), wiek (int), średnią
#ocen (float) i status studenta (bool). Wyświetl na ekranie wartość i typ każdej zmiennej.  


name = "Jan"  #str
age = 25  #int      
average_grade = 4.5  #float
is_student = True  #bool
#użyłem F-stringów do wyświetlenia wartości i typu każdej zmiennej w czytelny sposób
print(f"Imię: {name}, Typ: {type(name)}") 
print(f"Wiek: {age}, Typ: {type(age)}")
print(f"Średnia ocen: {average_grade}, Typ: {type(average_grade)}")
print(f"Status studenta: {is_student}, Typ: {type(is_student)}")
