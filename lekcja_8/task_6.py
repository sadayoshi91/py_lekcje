# Przerzucanie wyjątku: Napisz funkcję przetworz_dane(dane) , która w bloku
# try...except łapie KeyError (np. przy próbie dostępu do nieistniejącego klucza w
# słowniku), loguje go, a następnie rzuca ( raise ) nowy, własny wyjątek
# BladPrzetwarzaniaDanychError z informacją, którego klucza brakowało

DANE = {"raz": 1, "dwa": 2, "trzy": 3}

class BladPrzetwarzaniaDanychError(Exception):
    pass

def przetworz_dane(klucz: str):

    try:
        info = DANE[klucz]
        print(info)
    except KeyError:
        print("Nie ma takiego klucza")
        raise BladPrzetwarzaniaDanychError(f"Brakujący klucz: '{klucz}'")
    
przetworz_dane("raz")
przetworz_dane("tego_tutaj_nie_ma")