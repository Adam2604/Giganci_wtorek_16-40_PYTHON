"""Program zapyta o liczbę elementów, które ma przyjąć, a następnie odczyta od
użytkownika tyle komunikatów. Na koniec wyświetli je w tej samej kolejności.
"""

liczba_elementow = int(input("Podaj liczbę elementów: "))
elementy = []

for i in range(liczba_elementow):
    komunikat = input(f"Podaj element numer {i}: ")
    elementy.append(komunikat)
    #Sposób skrócony
    #elementy.append(input(f"Podaj element numer {i}"))

print(elementy)

#1 sposób
# for i in range(len(elementy)):
#     print(elementy[i])

#2 sposób
for element in elementy:
    print(element)