"""
Napisz program, który wczyta od użytkownika oceny końcowe z pięciu
przedmiotów: matematyka, polski, angielski, informatyka, wf. Następnie wyliczy
średnią ocen i wyświetli komunikat czy otrzymamy pasek na świadectwie
(aby otrzymać czerwony pasek nasza średnia musi być większa lub równa 4.75)."""

print("Podaj oceny końcowe z następujących przedmiotów: ")
matematyka = float(input("Matematyka: "))
polski = float(input("Polski: "))
angielski = float(input("Angielski: "))
informatyka = float(input("Informatyka: "))
wf = float(input("WF: "))

if matematyka < 1 or matematyka > 6 or polski < 1 or polski > 6 or angielski < 1 or angielski > 6 or informatyka < 1 or informatyka > 6 or wf < 1 or wf > 6:
    print("Wprowadzono błędne dane")
    exit()

srednia = (matematyka + polski + angielski + informatyka + wf) / 5
"""
lub w taki sposób:
suma = matematyka + polski + angielski + informatyka + wf
srednia = suma / 5
"""
if srednia >= 4.75:
    print("Gratulacje, masz świadectwo z paskiem")
else:
    print("Niestety nie otrzymasz w tym roku paska na świadectwie")
print(f"Twoja średnia to: ", srednia)