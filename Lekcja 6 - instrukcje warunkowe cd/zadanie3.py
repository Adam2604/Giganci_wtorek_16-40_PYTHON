"""
Napisz program, który wczyta od użytkownika długości trzech boków trójkąta, a

następnie:
1. Sprawdzi, czy taki trójkąt może istnieć:
○ Każdy bok musi być większy od zera.
○ Suma długości dwóch krótszych boków musi być większa niż długość
najdłuższego.
○ Jeśli te warunki nie są spełnione – wyświetl odpowiedni komunikat i
zakończ program.
2. Wyświetli:
○ Najkrótszy i najdłuższy bok.
○ Rodzaj trójkąta ze względu na długości boków:
➤ równoboczny – wszystkie boki równe
➤ równoramienny – dwa boki równe
➤ różnoboczny – wszystkie boki różne
○ Obwód trójkąta.
○ Rodzaj trójkąta ze względu na kąty:
➤ prostokątny – spełnia twierdzenie Pitagorasa
➤ rozwartokątny – największy kąt > 90°
➤ ostrokątny – wszystkie kąty < 90°"""

#Boki trójkąta
a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))
c = float(input("Podaj długość trzeciego boku: "))

#Podsumowanie boków
print(f"Podano boki: {a} {b} {c}")

najkrotszy = min(a, b, c)
najdluzszy = max(a, b, c)
obwod = a + b + c
sredni_bok = obwod - najkrotszy - najdluzszy

if a <= 0 or b <= 0 or c <= 0 or najdluzszy >= sredni_bok + najkrotszy:
    print("Podane boki nie utworzą trójkąta")
    exit() #Wcześniejsze zakończenie programu

#Zaczynamy część drugą programu
#Najpierw wypisanie najkrótszego i najdłuższego boku
print(f"Najkrótszy bok: {najkrotszy}")
print(f"Najdłuższy bok: {najdluzszy}")

#Sprawdzenie trójkąta ze względu na boki
if a == b == c:
    print("To jest trojkąt równoboczny")
elif a != b != c:
    print("To jest trójkąt różnoboczny")
else:
    print("To jest trójkąt równoramienny")

#wyświetlenie obwodu
print(f"Obwód trójkąta: {obwod}")

#Rodzaj trójkąta ze względu na kąty
"""
najdluzszy^2 ?? sredni_bok^2 + najkrotszy^2
prostokątny -> obie wartości będą równe
ostrokątny -> suma kwadratów dwóch boków jest większa
rozwartokątny -> kwadrat najdłuższego boku jest większy
"""
kwadrat_najdluzszego = najdluzszy ** 2
suma_kwadratow_dwoch = sredni_bok ** 2 + najkrotszy ** 2

if kwadrat_najdluzszego == suma_kwadratow_dwoch:
    print("Jest to trojkąt prostokątny")
elif suma_kwadratow_dwoch > kwadrat_najdluzszego:
    print("Jest to trójkąt ostrokątny")
else:
    print("Jest to trojkat rozwartokątny")
    