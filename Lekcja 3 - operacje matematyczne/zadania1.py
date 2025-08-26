# #pobranie wartości z konsoli od użytkownika
# input()
# #zapisanie do zmiennej
# x = input()
# #można też dodać wiadomość
# imie = input("Podaj swoje imię: ")
# print(imie)

# #zmienna liczbowa pobrana z input()
# wiek = int(input("Podaj swój wiek: "))
# print(type(wiek))

# CTRL + / -> zakomentowanie

#Operacje matematyczne
a = 10
b = 7
print(a + b) #17
print(a - b) #3
print(a * b) #70
print(a / b) #1.4285714285714286
print(10 / 5) #operator dzielenia ZAWSZE zwraca wartość typu float
print(a % b) #3 -> operator dzielenia modulu, zwraca resztę z dzielenia pierwszej liczby przez drugą
print(a // b) #1 -> operator dzielenia całkowitego, zaokrągla w dół
print(3 ** 2) #9 -> operator potęgowania

#Działania na zmiennych w trakcie działania programu
a = 3
b = 4
#jak zwiększyć liczbę o 2?
a = a + 2
print(a)
#szybszy sposób
a += 2
print(a)
#pozostałe operacje
a -= 5
print(a)

b *= a #taki sam zapis jak b = b * a
print(b)

b /= 2
print(b)

a %= 2
print(a)

a = 7
a //= 2
print(a)

b **= a #4 do potęgi 3
print(b)

#operacje na zmiennych typu bool
print(True + True) #2
print(False + True) #1
print(3*True) #3


#operacje na zmiennych typu string
#dodawanie
print("Witaj " + "Gigancie") #Witaj Gigancie

#mnożenie
print(3 * "test ")
print("test " * 3)

tekst = "tekst"
nowy_tekst = "nowy "
nowy_tekst += tekst
print(nowy_tekst)

#możemy też wypisywać stringi łącząc je z innymi danymi
x = 10
y = 25
print("Wynik mnożenia", x, "przez", y, "wynosi", x*y)
print(f"Wynik dodawania {x} i {y} wynosi {x+y}")

#Funkcje wbudowane
print(abs(-10)) #funkcja abs() zwraca liczbę bezwzględną
print(max(1, 3, 5, 2, -5, 4)) #funkcja max() zwraca największą liczbę z podanych
print(min(1, 3, 5, 2, -5, 4)) #funkcja min() zwraca najmniejszą liczbę z podanych
print(round(3.789)) # zaokrąglenie liczby
print(len("Hello world")) #zwraca długość obiektu