#Kalkulator BMI: Napisz program, który zapyta użytkownika o jego wagę w kilogramach i
#wzrost w metrach. Oblicz i wyświetl wskaźnik masy ciała (BMI) według wzoru: BMI = waga
#/ (wzrost * wzrost) .

weight = float(input("Podaj swoją wagę w kilogramach: "))  #pobieram wagę od użytkownika i konwertuję na float
height = float(input("Podaj swój wzrost w metrach: "))
bmi = weight / (height * height)  #obliczam BMI według wzoru
print(f"Twoje BMI wynosi: {bmi:.2f}")  
