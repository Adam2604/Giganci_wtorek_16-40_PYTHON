"""
Napisz funkcję, która zwraca listę losowych liczb. Rozmiar listy zależy od argumentu.
Dodatkowo: Funkcja powinna otrzymać dwa dodatkowe argumenty: minimalna i
maksymalna wartość, która może zostać wylosowana."""

import random

def losowe(rozmiar, minimum, maksimum):
    lista = []
    for i in range(rozmiar):
        lista.append(random.randint(minimum, maksimum))
    return lista

print(losowe(10, 0, 20))