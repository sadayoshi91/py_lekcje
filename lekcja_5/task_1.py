# Napisz program, który pobiera od użytkownika wiek. Używając instrukcji
# if-elif-else , wyświetl jeden z komunikatów: "Niemowlę" (0-1), "Dziecko" (2-12),
# "Nastolatek" (13-17), "Dorosły" (18-64), "Senior" (65+)

age = int(input("Podaj wiek: "))

if age <= 1:
    print("Niemowlę")
elif age <= 2 <= 12:
    print("Dziecko")
elif age <= 13 <= 17:
    print("Nastolatek")
elif age <= 18 <= 64:
    print("Dorosły")
elif age >= 65:
    print("Senior")
else:
    print("Podaj poprawny wiek")