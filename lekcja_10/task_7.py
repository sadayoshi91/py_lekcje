class Telewizor:
    def __init__(self):
        self.kanal = 1
        self.glosnosc = 10
        self.__wlaczony = False
    
    def wlacz(self):
        self.__wlaczony = True

    def wylacz(self):
        self.__wlaczony = False

    def zmien_kanal(self, numer):
        if self.__wlaczony:
            self.kanal = numer
    
    def glosniej(self):
        if self.__wlaczony:
            if self.glosnosc + 10 >= 0 and self.glosnosc + 10 <= 100:
                self.glosnosc += 10

    def ciszej(self):
        if self.__wlaczony:
            if self.glosnosc - 10 >= 0 and self.glosnosc - 10 <= 100:
                self.glosnosc -= 10
    
    def info(self):
        print(f"Status: {self.__wlaczony}, kanał: {self.kanal}, głośność: {self.glosnosc}")

tv = Telewizor()

tv.wlacz()
tv.info()
tv.ciszej()
tv.info()
tv.ciszej()
tv.info()
tv.zmien_kanal(5)
tv.info()

for i in range(0, 11):
    tv.info()
    tv.glosniej()

tv.info()
tv.wylacz()