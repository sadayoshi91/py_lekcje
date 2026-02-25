# Utwórz zmienną x = 10. Wyświetl id(x). Wykonaj x = x + 0 (dodaj zero). Wyświetl id(x)
# ponownie. Czy się zmienił? A teraz utwórz listę y = \[1, 2\]. Wyświetl id(y). Dodaj element:
# y.append(3). Wyświetl id(y). Czy się zmienił? Wyjaśnij różnicę w komentarzu.
# Wskazówka: int jest niemutowalny — nawet x + 0 tworzy nowy obiekt. Lista jest mutowalna —
# append() zmienia ten sam obiekt.

x = 10
print(id(x))
