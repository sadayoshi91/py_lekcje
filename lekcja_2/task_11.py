#poproś użytkownika o parametry funkcji kwadratowej ax^2 + bx + c (a, b, c)
a = float(input("Podaj wartość a: "))
b = float(input("Podaj wartość b: "))   
c = float(input("Podaj wartość c: "))
delta = b**2 - 4*a*c  #obliczamy deltę
if delta < 0: # delta musi być większa lub równa 0 aby istniały rozwiązania rzeczywiste
    print("Brak rozwiązań rzeczywistych")
elif delta == 0: # jedno podwójne rozwiązanie
    x = -b / (2*a)
    print(f"Jedno podwójne rozwiązanie: x = {x}")
else: # dwa różne rozwiązania
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print(f"Dwa różne rozwiązania: x1 = {x1}, x2 = {x2}")
