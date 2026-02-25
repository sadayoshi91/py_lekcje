# Utwórz dwie zmienne a = 100 i b = 100. Sprawdź a is b i a == b. Powtórz dla a = 1000 i b =
# 1000. Powtórz dla a = "hello" i b = "hello". Wyświetl wyniki id() i porównań.
# Wskazówka: Małe liczby i krótkie stringi mogą współdzielić obiekt. Duże liczby raczej nie.

# Przypadek 1: małe liczby
a = 100
b = 100
print("a = 100, b = 100")
print("a == b:", a == b)
print("a is b:", a is b)
print("id(a):", id(a))
print("id(b):", id(b))
print()

# Przypadek 2: duże liczby
a = 1000
b = 1000
print("a = 1000, b = 1000")
print("a == b:", a == b)
print("a is b:", a is b)
print("id(a):", id(a))
print("id(b):", id(b))
print()

# Przypadek 3: string
a = "hello"
b = "hello"
print('a = "hello", b = "hello"')
print("a == b:", a == b)
print("a is b:", a is b)
print("id(a):", id(a))
print("id(b):", id(b))