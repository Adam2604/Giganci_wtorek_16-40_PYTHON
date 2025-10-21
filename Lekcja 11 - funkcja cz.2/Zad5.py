"""
Napisz funkcję, która otrzymuje liczbę całkowitą a zwraca sumę jej cyfr.
Dla liczby 249 otrzymujemy 2+4+9 czyli 15"""

#w funkcji:
#1. zmienić liczbę(int) na tekst(str)
#2. w pętli przejdziemy po całej liczbie przez wszystkie cyfry
#3. do zmiennej suma będziemy dodawać liczby, które najpierw spowrotem zamienimy z str na int

def suma_cyfr(liczba):
    suma = 0
    zamiana = str(abs(liczba))
    for cyfra in zamiana:
        suma += int(cyfra)
    return suma

print(suma_cyfr(-249))