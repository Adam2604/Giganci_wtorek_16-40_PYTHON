#Pobierz od użytkownika liczbę, a następnie wartość procentową. Program
#ma za zadanie wyświetlić ile to jest ( % z liczby )
#Dla podanych danych: 100 i 60 -> wynik: 60
#60% z liczby 100 wynosi 60

liczba = int(input("Podaj liczbę: "))
procent = int(input("Podaj procent: "))

#1 sposób
wynik = liczba * procent/100
print(f"{procent}% z {liczba} wynosi {wynik}")

#2. sposób
print(f"{procent}% z {liczba} wynosi {liczba * procent/100}")
