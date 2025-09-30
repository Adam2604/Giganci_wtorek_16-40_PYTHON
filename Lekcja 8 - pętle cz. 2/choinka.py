"""Napisz program, który zapyta użytkownika o wysokość (liczbę linijek), a następnie
wyświetli choinkę / piramidę o podanej wysokości. Choinka ma składać się z gwiazdek
‘*’ oraz spacji jako znaków białych."""

linijki = int(input("Podaj liczbę linijek: "))
if linijki < 0:
    print("Nie można utworzyć takiej choinki")
else:
    for i in range(1,linijki+1):
        spacje = " " * (linijki - i)
        gwiazdki = "* " * i
        print(spacje + gwiazdki)


"""
Przykład dla 5 linijek:
i = 1 -> spacje = 4, gwiazdki = 1
i = 2 -> spacja = 3, gwiazdki = 3
i = 3 -> spacja = 2, gwiazdki = 5
i = 4 -> spacja = 1, gwiazdki = 7
i = 5 -> spacja = 0, gwiazdki = 9

    *
   ***
  *****
 *******
*********
"""