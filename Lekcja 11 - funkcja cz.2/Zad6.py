"""Napisz funkcję, która zapyta użytkownika o hasło i login. Funkcja ma zwrócić True, jeśli
podano poprawne hasło i login lub False w innym przypadku."""

def logowanie(popr_login: str, popr_haslo: str) -> bool:
    login = input("Podaj login: ")
    haslo = input("Podaj hasło: ")

    if login == popr_login and haslo == popr_haslo:
        return True
    else:
        return False
    
    #krótsza wersja:
    #return login == popr_login and haslo == popr_haslo

print(logowanie("admin", "masło"))