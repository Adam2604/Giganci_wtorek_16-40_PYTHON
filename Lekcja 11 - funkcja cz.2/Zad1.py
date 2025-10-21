"""
Przygotuj funkcję, która jako argument otrzymuje string oraz listę stringów, a zwraca
napis, gdzie pomiędzy elementy z listy dokładana jest zawartość pierwszego
argumentu. Wskazówka: skorzystaj z metody join"""

#Przykład:
#Pierwszy argument: !
#Drugi argument ["Ala", "ma", "kota"]
#Wynik funkcji: Ala!ma!kota

def polacz(znak, slowa):
    nowe_slowo = slowa[0]

    for element in slowa[1:]:
        nowe_slowo += znak
        nowe_slowo += element

    return nowe_slowo

print(polacz(" ", ["Ala", "ma", "kota"]))



