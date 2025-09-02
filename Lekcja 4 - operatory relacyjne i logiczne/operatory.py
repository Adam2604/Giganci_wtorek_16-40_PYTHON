250 > 42.01 # 250 jest większe niż 42.01 # Prawda
490 <= 450 # 490 jest mniejsze lub równe od 450 # Fałsz
24 == 12 # 24 jest równe 12 # Fałsz
40 != 23 # 40 jest różne od 23 # Prawda
40 > 40 # 40 jest większe od 40 # Fałsz
99 < 98.5 # 99 jest mniejsze od 98.5 # Fałsz

print(12 == 15) # Fałsz # ==, <, !=, <=
print(5 <= 15000) # Prawda # ==, >, >=, <=
print(120 != 120) # Fałsz # ==, >=, !=, <=
print(60 == 15) # Fałsz # ==, <, !=, >=
print(25.3421 == 25.3421) # Prawda # ==, <, !=, <=

# print("Czy możesz skorzystać z roller-coastera?")
# print("True - możesz skorzystać z roller-coastera")
# print("False - nie możesz skorzystać z roller-coastera")

# wzrost_cm = int(input("Podaj swój wzrost w centymetrach: "))
# print(wzrost_cm >= 150)

#Operatory logiczne
#1. Operator jednoargumentowy NOT
not True #Wynik: False
not False #Wynik: True

#Przykład 1
not 50 == 51

#Przykład 2
not(not 4>10)

#2. Operator dwuargumentowy AND
True and True #Wynik: True
True and False #Wynik: False
False and True #Wynik: False
False and False #Wynik: False

#Przykład 1
20 < 25 and 24 > 1 #Wynik: False

#Przykład 2
2 < 5 and 10 != 5 #Wynik: True

#3. Operator dwuargumentowy OR
True or True #Wynik: True
True or False #Wynik: True
False or True #Wynik: True
False or False #Wynik: False

#Przykład 1
20 < 25 or 24 > 1 #Wynik: True

#Przykład 2
5 < 2 or 10 == 5 #Wynik: False