import getpass

"""
Napisz program, który będzie działał jak podstawowy system logowania.

Wykonaj poniższe kroki:
1. Zapisz dane do logowania w zmiennych:
○ LOGIN = "gigant@trener.pl"
○ HASLO = "qwerty"
2. Poproś użytkownika o podanie loginu (za pomocą input()).
3. Poproś użytkownika o podanie hasła.
4. Sprawdź, czy wprowadzone dane są zgodne z zapisanymi loginem i hasłem:
○ jeśli tak – wyświetl komunikat: "Poprawnie zalogowano"
○ jeśli nie – wyświetl komunikat: "Niepoprawny login lub hasło"""

LOGIN = "gigant@trener.pl"
HASLO = "qwerty"

user_login = input("Login: ")
user_haslo = getpass.getpass("Hasło: ")

if user_login == LOGIN and user_haslo == HASLO:
    print("Poprawnie zalogowano")
else:
    print("Niepoprawy login lub hasło")