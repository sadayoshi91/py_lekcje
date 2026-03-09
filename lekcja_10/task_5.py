PI = 3.14159

class Figura:
    def __init__(self):
        pass
    def oblicz_pole(self):
        print("Ta figura nie ma pola")
        pass

class Kwadrat(Figura):
    def __init__(self, bok):
        self.bok = bok
    def oblicz_pole(self):
        return self.bok * self.bok

class Kolo(Figura):
    def __init__(self, promien):
        self.promien = promien
    def oblicz_pole(self):
        return self.promien ** 2 * PI
    

moj_kwadrat = Kwadrat(10)
moje_kolo = Kolo(10)

moje_figury = [moj_kwadrat, moje_kolo]

for i in moje_figury:
    print(i.oblicz_pole())