"""Napisz funkcję, która przyjmuje następujące argumenty: imie (str), wiek (int), wzrost_m
(float), a zwraca napis: “Jan, lat 20, 1.75 m wzrostu” - oczywiście argumenty należy
podstawić do szablonu. Wzrost ma zawsze pokazywać dwa miejsca po przecinku."""

def komunikat(imie: str, wiek: int, wzrost: float) -> str:
    return f"{imie}, lat {wiek}, {wzrost:.2f} m wzrostu"

print(komunikat("Jan", 25, 1.780899872984))