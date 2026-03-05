def oblicz_srednia(lista_ocen):
    assert len(lista_ocen) > 0
    return sum(lista_ocen)/len(lista_ocen)


print(oblicz_srednia([1, 2, 3]))

print(oblicz_srednia([]))