"""
Napisz program, który zapyta użytkownika o N ocen cząstkowych, a następnie wyliczy
średnią z przedmiotu.
N - liczba ocen wprowadzona przez użytkownika na początku działania programu"""

N = int(input("Podaj liczbę ocen: "))
suma = 0
for i in range(N):
    ocena = float(input("Podaj ocene: "))
    suma += ocena

srednia = suma / N
print(f"Twoja średnia wynosi {srednia}")
