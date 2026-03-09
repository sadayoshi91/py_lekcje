# Zaprojektuj hierarchię klas: Instrument -> Strunowy i Dety. Następnie Gitara (dziedziczy po
# Strunowy) i Trabka (dziedziczy po Dety). Klasa Instrument powinna mieć metodę graj(),
# która zwraca ogólny komunikat. Każda kolejna klasa w hierarchii powinna nadpisywać tę
# metodę, dodając coś od siebie i wywołując wersję z klasy nadrzędnej za pomocą
# super().graj().
# Instrument.graj() -> "Wydaje dźwięk."
# Strunowy.graj() -> "Wydaje dźwięk. [Szarpnięcie struny]"
# Gitara.graj() -> "Wydaje dźwięk. [Szarpnięcie struny] [Akord G-dur]"


class Instrument:
    def graj(self) -> str:
        return "Wydaje dźwięk."


class Strunowy(Instrument):
    def graj(self) -> str:
        return super().graj() + " [Szarpnięcie struny]"


class Dety(Instrument):
    def graj(self) -> str:
        return super().graj() + " [Dmuchnięcie powietrza]"


class Gitara(Strunowy):
    def graj(self) -> str:
        return super().graj() + " [Akord G-dur]"


class Trabka(Dety):
    def graj(self) -> str:
        return super().graj() + " [Fanfara]"


gitara_1 = Gitara()
print(gitara_1.graj()) 

trabka_1 = Trabka()
print(trabka_1.graj())

    
