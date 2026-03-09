# Stwórz następującą, złożoną hierarchię dziedziczenia:
# class A
# class B(A)
# class C(A)
# class D(B)
# class E(C)
# class F(D, E) Narysuj schemat tej hierarchii w mermaid. Następnie, nie uruchamiając
# kodu, spróbuj przewidzieć, jakie będzie MRO dla klasy F. Na koniec sprawdź swoją
# odpowiedź, używając print(F.mro()).

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B):
    pass

class E(C):
    pass

class F(D, E):
    pass
# Do wizualizacji użyłem https://mermaid.live 
# Schemat hierarchii w mermaid:
# 
# ```mermaid
# classDiagram
#     A <|-- B
#     A <|-- C
#     B <|-- D
#     C <|-- E
#     D <|-- F
#     E <|-- F
# ```

# Przewidywane MRO dla klasy F:
# F, D, B, E, C, A, object

print(F.mro())