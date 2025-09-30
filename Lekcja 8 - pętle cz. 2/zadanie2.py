"""
Napisz program, który wypisze w konsoli tabliczkę mnożenia. Wykorzystaj funkcję
str(liczba).center(liczba_znaków) do wyrównania tekstu."""

for a in range(1,11):
    linia = ""
    for b in range(1,11):
        linia += str(a*b).center(4) + "|"
        pass
    print(linia)
    pass