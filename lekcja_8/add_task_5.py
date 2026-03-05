#  Własny wyjątek z kontekstem
# Zdefiniuj wyjątek TemperaturaKrytycznaError przechowujący temperaturę i limit. Napisz funkcję
# sprawdz_temperature(temp, limit=100), która rzuca ten wyjątek gdy temp > limit.
# Wskazówka: class TemperaturaKrytycznaError(Exception): def __init__(self, temp, limit): ...

class TemperaturaKrytycznaError(Exception):
    def __init__(self, temp, limit):
        self.temp = temp
        self.limit = limit
        super().__init__(f"Temperatura {temp} przekracza limit {limit}")

def sprawdz_temperature(temp, limit=100):
    if temp > limit:
        raise TemperaturaKrytycznaError(temp, limit)
    else:
        print(f"Temperatura {temp} jest bezpieczna, nie przekracza limitu {limit}.")
        return temp
try:
    sprawdz_temperature(120)
except TemperaturaKrytycznaError as error:
    print(f"Wystąpił błąd: {error}")


