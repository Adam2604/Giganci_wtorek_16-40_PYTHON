"""Napisz program, który wczyta od użytkownika dwie liczby: wysokość i szerokość, a
następnie wypisze w konsoli prostokąt składający się z gwiazdek.
Przykład dla wysokości = 3, szerokości = 5:
*****
*****
*****
"""

wysokosc = int(input("Podaj wysokość prostokąta: "))
szerokosc = int(input("Podaj szerokość prostokąta: "))

for i in range(wysokosc):
    print("*" * szerokosc)

