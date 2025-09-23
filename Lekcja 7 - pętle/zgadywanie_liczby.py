import random

minimum = 0
maximum = 100

#wyloswanie wartości i zapisanie jej do zmiennej
wylosowana_liczba = random.randint(minimum, maximum)

odpowiedz = None
licznik_tur = 0

while odpowiedz != wylosowana_liczba:
    odpowiedz = int(input("Podaj liczbę: "))
    licznik_tur += 1

    if odpowiedz < wylosowana_liczba:
        print("Za mało")
    elif odpowiedz > wylosowana_liczba:
        print("Za dużo")

print("Gratulacje, udało ci się odgadnąć wylosowaną liczbę!")
print(f"Liczba: {wylosowana_liczba}")
print(f"Odgadłeś liczbę w {licznik_tur} turach")