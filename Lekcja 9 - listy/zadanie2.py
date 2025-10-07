#Oblicz średnią z wprowadzonych ocen

oceny = []

while True:
    ocena = input("Podaj ocenę: ")

    if ocena == "q":
        break

    ocena = float(ocena)
    oceny.append(ocena)
    print(oceny)

suma = sum(oceny)
srednia = suma / len(oceny)
print(f"Twoja średnia wynosi {srednia}")