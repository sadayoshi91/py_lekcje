# Dekorator z argumentem: Stwórz dekorator @powtorz(n) , który przyjmuje argument n i
# powoduje, że udekorowana funkcja zostanie wykonana n razy.

def repeat(n): # przyjmuje argument dekoratora
    def decorator(func): # przyjmuje funkcję
        def wrapper(*args, **kwargs): # wywołanie funkcji
            result = None
            for _ in range(n): # użycie _ zamiast określonej zmiennej
                result = func(*args, ** kwargs) # używam args i kwargs aby nie przyjmować sztywno okreslonych zmiennych
            return result
        return wrapper
    return decorator

@repeat(3) # w () liczba powtórzeń która jest definiowana przez n w def repeat(n)
def welcome(): # wywłoanie nowej funkcji poprzez dekorator 
    print("Cześć!")

print(welcome()) # zwraca none bo nie ma return w welcome()