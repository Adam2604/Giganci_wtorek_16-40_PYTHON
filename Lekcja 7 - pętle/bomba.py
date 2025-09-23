import time

liczba = int(input("Wprowadź liczbę: "))
while liczba > 0:
    print("\r" + str(liczba), end = "")
    liczba -= 1
    time.sleep(1)

print("\r" + "BOOM!")