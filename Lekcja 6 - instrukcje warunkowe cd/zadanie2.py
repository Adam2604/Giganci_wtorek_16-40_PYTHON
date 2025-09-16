"""
Stwórz program, który obsłuży proces dwuetapowego logowania. Użytkownik
zostanie poproszony o wprowadzenie czterocyfrowego PINu. Jeśli poda błędny
PIN, program wyświetli odpowiedni komunikat o błędzie. W przypadku poprawnego
PINu, użytkownik zostanie następnie poproszony o podanie hasła słownego.

PIN: „1234”
Hasło: „Masło” """

PIN = "1234"
HASLO = "Masło"

user_pin = input("Podaj pin: ")
if user_pin == PIN:
    user_haslo = input("Podaj Hasło: ")
    if user_haslo == HASLO:
        print("Poprawnie zalogowano")
    else:
        print("Wprowadzono błędne hasło")
else:
    print("Wprowadzono błędny pin")