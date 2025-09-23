pin = "1234"
rok = "2004"
haslo = "masło"

while True:
    user_pin = input("PIN: ")
    if user_pin != pin:
        print("Odmowa dostępu!")
        continue

    user_rok = input("Rok urodzenia: ")
    if user_rok != rok:
        print("Odmowa dostępu, zaloguj się ponownie!")
        continue

    user_haslo = input("Podaj hasło: ")
    if user_haslo != haslo:
        print("Odmowa dostępu, zaloguj się ponownie!")
        continue

    print("Zalogowano pomyślnie!")
    break

print("Super tajne treści znajdują się tutaj")