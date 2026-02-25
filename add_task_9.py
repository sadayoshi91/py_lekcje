# Napisz dekorator @zbierz_wyniki(n), który wywołuje funkcję n razy i zwraca listę wszystkich
# wyników.
# Wskazówka: Trzy poziomy jak w sekcji 2.8. W wrapper: wyniki = \[\], w pętli dodawaj
# wyniki.append(funkcja(*args, **kwargs)). Return wyniki.

def take_results(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(n):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@take_results(3)
def new_res(a):
    return a * 2

print(new_res(10))