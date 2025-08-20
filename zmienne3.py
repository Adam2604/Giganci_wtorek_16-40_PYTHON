# Konwersje zmiennych - zmiana typów

# 1. Konwersja do typu int
liczba = int(3.2)
print(liczba, type(liczba))
liczba = int(True)
print(liczba, type(liczba))
liczba = int(False)
print(liczba, type(liczba))
liczba = int("10")
print(liczba, type(liczba))
# liczba = int("Tekst")
# print(liczba, type(liczba)) - to nie zadziała

#CTRL + / -> zakomentowywanie i odkomentowywanie zaznaczonych linijek

# 2. Konwersja do typu bool
prawda = bool(1)
print(prawda, type(prawda))
falsz = bool(0)
print(falsz, type(falsz))
liczba = bool(-5)
print(liczba, type(liczba))

# 3. Konwersja do typu float
liczba = float(5)
print(liczba, type(liczba))
liczba = float("25.5")
print(liczba, type(liczba))

# 4. Konwersja do typu str
tekst = str(15)
print(tekst, type(15))
tekst = str(False)
print(tekst, type(tekst))
