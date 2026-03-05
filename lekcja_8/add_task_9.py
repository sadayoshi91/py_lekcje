#  Retry z limitem prób
# Napisz funkcję wykonaj_z_retry(funkcja, max_prob=3) która wywołuje podaną funkcję. Jeśli rzuci
# wyjątek — próbuje ponownie, maksymalnie max_prob razy. Jeśli wszystkie próby się nie powiodą
# — rzuca ostatni wyjątek.
# Wskazówka: Pętla for i in range(max_prob): try/except. W except: zapisz wyjątek. Po pętli: raise
# ostatni_wyjatek.

def do_with_retry(func, max_prob=3):
    last_exception = None
    for _ in range(max_prob):
        try:
            return func()
        except Exception as e:
            last_exception = e
            print(f"Wystąpił błąd: {e}. Próba ponowienia...")
    if last_exception is not None:
        raise last_exception
