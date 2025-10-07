ocena_nr_1 = 5
ocena_nr_2 = 3
ocena_nr_3 = 2
ocena_nr_4 = 4
ocena_nr_5 = 5
ocena_nr_6 = 2

#To samo ale za pomocą listy:
oceny = [5,3,2,4,5,2]

#Jakie typy danych mogą przechowywać listy?
moja_lista = [2, "Napis", 5.5, True, ["Kolejna", 0, "Lista"], 10]

moja_lista2 = [2, "Napis", 5.5,
            True, ["Kolejna", 0, "Lista"],
            10]
print(moja_lista2)


#Indeksowanie
oceny =     [5, 3, 2, 4, 5, 2]
#Indeksy     0  1  2  3  4  5
print(oceny[3])

dodawanie_ocen = oceny[1] + oceny[3]
print(dodawanie_ocen)

liczby = [1,2,3,4,5,3,1,3,4,2,1,2,3,4,6,7,4,2,13]
#Zakres <start; stop) 
nowa_lista = liczby[2:6]

nowa_lista1 = liczby[:5] #od początku listy do 5 indeksu
nowa_lista2 = liczby[8:] #od 8 indeksu do końca listy
print(nowa_lista2)