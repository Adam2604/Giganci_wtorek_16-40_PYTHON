"""
Napisz funkcję, która jako argument otrzymuje listę elementów, w której mogą
występować powtórzenia, a zwraca listę unikalnych elementów.
Dla [1,2,3,3,3,3,4,5] oczekujemy [1, 2, 3, 4, 5]"""

def unikalne(lista):
    unikalna = []
    for element in lista:
        if element not in unikalna:
            unikalna.append(element)
    return unikalna

print(unikalne([2,5,4,2,3,4,2,1,2,3,46,5]))