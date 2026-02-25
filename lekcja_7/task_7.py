# Dekorator logujący: Napisz dekorator @loguj , który przed wywołaniem udekorowanej
# funkcji wypisze komunikat Uruchamiam funkcję [nazwa_funkcji]... , a po jej
# zakończeniu Zakończono funkcję [nazwa_funkcji].

def login(func):

    def wrapper(*args, **kwargs):
        print(f"Uruchamiam funkcję add_sum...")
        result = func(*args, **kwargs)
        print(f"Zakończono funkcję add_sum")
        return result

    return wrapper


@login # wywłujemy dekorator
def add_sum(a, b):
    return a + b


print(add_sum(5, 293))
