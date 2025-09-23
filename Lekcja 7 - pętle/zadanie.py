"""
Napisz program w Pythonie, który działa jak licznik zgadywania hasła:

1.Program w pętli while pyta użytkownika o hasło.

2.Jeśli użytkownik wpisze "tajne" – wyświetl komunikat "Dostęp przyznany!" i zakończ program

3. Jeśli użytkownik wpisze "pomiń" – wyświetl komunikat "Ta próba została pominięta." i przejdź do kolejnej iteracji 

4.W innym przypadku wyświetl komunikat "Błędne hasło, spróbuj ponownie." i dalej pytaj."""

while True:
    haslo = input("Podaj hasło: ")
    if haslo == "tajne":
        print("Dostęp przyznany")
        break
    elif haslo == "pomiń":
        print("Ta próba została zamknięta!")
        continue
    print("Błędne hasło, spróbuj ponownie.")