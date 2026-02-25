#Utwórz zmienną tekst = "25". Zamień na int, potem na float, potem na bool, potem z powrotem
#na str. Na każdym kroku wyświetl wartość i typ.

text = "25"

text_int = int(text)
print(text_int, type(text_int))
text_float = float(text_int)
print(text_float, type(text_float))
text_bool = bool(text_float)
print(text_bool, type(text_bool))
text_str = str(text_bool)
print(text_str, type(text_str))