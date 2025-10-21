"""
Napisz funkcję, która otrzyma dwa argumenty pierwszym będzie liczba, którą chcemy
podzielić bez reszty a drugim argumentem będzie dzielnik. Należy sprawdzić czy
można dokonać dzielenia a jeśli tak zwrócić informację czy liczba jest podzielna bez
reszty czy nie."""

def dzielenie(liczba, dzielnik):
    if dzielnik == 0:
        return "Nie można dzielić przez 0!"
    elif liczba % dzielnik == 0:
        return f"Liczba {liczba} jest podzielna przez {dzielnik}"
    else:
        return f"Liczba {liczba} nie jest podzielna przez {dzielnik}"
    
print(dzielenie(5, 0))
print(dzielenie(4, 2))
print(dzielenie(5, 3))