#Zapis instrukcji warunkowej
print("Wykonam się za każdym razem")
warunek = False
if warunek:
    #Tutaj będzie kod, który się wykona tylko wtedy warunek jest prawdziwy
    print("Warunek był prawdziwy")
print("Wykonam się za każdym razem bo nie ma już wcięcia")

# dzielna = int(input("Wprowadź dzielną: "))
# dzielnik = int(input("Wprowadź dzielnik: "))

# if dzielnik != 0:
#     wynik = dzielna/dzielnik
#     print(f"Wynik z dzielenia: {wynik}")

# if dzielnik == 0:
#     print("Nie wolno dzielić przez zero")

#Konstrukcja if-else
if warunek:
    pass
else:
    #Ta cześć kodu się wykona jeżeli warunek nie był spełniony
    pass

dzielna = int(input("Wprowadź dzielną: "))
dzielnik = int(input("Wprowadź dzielnik: "))

if dzielnik != 0:
    wynik = dzielna/dzielnik
    print(f"Wynik z dzielenia: {wynik}")
else:
    print("Nie wolno dzielić przez zero!")
