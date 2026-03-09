class Wektor2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    # przeciążanie operacji +
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return(x, y)
    
    # przeciążanie operacji -
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return (x, y)

    # przeciążanie operacji ==
    def __eq__(self, other):
        #return self.x == other.x and self.y == other.y
        if self.x == other.x and self.y == other.y:
            return True
        
        return False
        
wektor_1 = Wektor2d(3, 3)
wektor_2 = Wektor2d(2, 3)

print(f"Dodawanie {wektor_1 + wektor_2}")
print(f"Odejmowanie {wektor_1 - wektor_2}")
print(f"Porównanie {wektor_1 == wektor_2}")
print(wektor_1)
print(wektor_2)