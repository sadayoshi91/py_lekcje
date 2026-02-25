#Zadanie 6
#Poproś użytkownika o:
#- wiek,
#- wzrost w cm,
#- wagę w kg,
#- informację czy uprawia sport (1 – tak, 0 – nie).
#Program powinien:
#1. Obliczyć BMI.
#2. Sprawdzić, czy:
#   - użytkownik jest pełnoletni,
#   - BMI mieści się w normie (18.5–25),
#   - użytkownik uprawia sport.
#3. Wyświetlić:
#"Kwalifikujesz się do programu zdrowotnego"
#lub
#"Nie kwalifikujesz się do programu zdrowotnego"

age = int(input("Podaj wiek: "))
height = float(input("Podaj wzrost w cm: "))
weight = float(input("Podaj wagę w kg: "))
info_sport = int(input("Czy uprawiasz sport? 1 - TAK, 0 - NIE: "))
# bmi = weight / height **
bmi = weight / (height * height)
bmi_float = float(bmi)
print(f"Twoje BMI to: {bmi_float}")
if age < 18:
    print("Użytkownik jest pełnoletni")
elif 18.5 <= bmi_float <= 25:
    pass
elif info_sport not in [0, 1]:
    print("Błędne dane! Musi być 0 lub 1")
elif info_sport == 0:
    print("Nie uprawiasz sportu - nie kwalifikujesz się")
else: 
    print("Kwalifikujesz się do programu zdrowotnego")
