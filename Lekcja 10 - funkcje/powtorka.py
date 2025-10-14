import random

liczba = int(input("Podaj liczbę: "))

lista = []
for i in range(liczba):
    lista.append(random.randint(0,100))

print(lista)