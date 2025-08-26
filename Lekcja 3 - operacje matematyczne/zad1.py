# Pobierz od użytkownika imię, nazwisko, rok urodzenia i wypisz na konsolę
# informację (dla danych Jan Kowalski, 1996): „Jan Kowalski ma rocznikowo 29 lat.”
imie = input("Podaj imie: ")
nazwisko = input("Podaj nazwisko: ")
rok_urodzenia = int(input("Podaj rok urodzenia: "))
print(f"{imie} {nazwisko} ma rocznikowo {2025 - rok_urodzenia} lat")


