"""Przygotuj program, który zapyta użytkownika o 3 różne liczby, każdą z nich wpisz do
zmiennej: kolejno a, b, c. Przygotuj trzy zmienne typu bool: czy_a_to_max,
czy_b_to_max, czy_c_to_max."""

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
c = int(input("Podaj liczbę c: "))

czy_a_to_max = a > b and a > c
czy_b_to_max = b > a and b > c
czy_c_to_max = c > a and c > b

print(f'a: {czy_a_to_max}')
print(f'b: {czy_b_to_max}')
print(f'c: {czy_c_to_max}')