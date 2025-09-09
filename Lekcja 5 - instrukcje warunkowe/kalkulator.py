'''
1. Program poprosi użytkownika o podanie pierwszej liczby.
2. Następnie wyświetli możliwe działania matematyczne, które można wykonać:
a. + → dodawanie
b. - → odejmowanie
c. * → mnożenie
d. / → dzielenie
Jeżeli starczy czasu program możemy wzbogacić o dodatkowe operacje
matematyczne. Warto poprosić uczniów o propozycje innych działań.
3. Użytkownik wpisuje znak wybranego działania.
4. Program prosi o drugą liczbę.
5. Na końcu program wyświetla wynik obliczenia.'''

a = float(input("Podaj pierwszą liczbę: "))

print("+ → dodawanie")
print("- → odejmowanie")
print("* → mnożenie")
print("/ → dzielenie")

symbol = input("Wybierz jedną z dostępnych operacji matematycznych")
b = float(input("Wprowadź drugą liczbę: "))

if symbol == "+":
    wynik = a + b
elif symbol == "-":
    wynik = a - b
elif symbol == "*":
    wynik = a * b
elif symbol == "/":
    if b == 0:
        print("Nie można dzielić przez zero!")
        wynik = "Błąd"
    else:
        wynik = a / b
else:
    print("Wprowadzono niepoprawny symbol")
    wynik = "Błąd"

print(f"{a}{symbol}{b}={wynik}")