wyraz = input("Podaj testowane słowo: ")

if "a" in wyraz or "d" in wyraz or "jku" in wyraz:
    print(wyraz, "posiada jedno z wyszukiwanych haseł")
else:
    print(wyraz, "NIE posiada żadnego z wyszukiwanych haseł")


#Instrukcje zagnieżdżone
if warunek:
    #Tutaj możemy też coś dopisać, instrukcję dla tego ifa wyżej
    if warunek2:
        #Kod wykonywany tylko wtedy jeżeli warunek i warunek2 są spełnione
        pass
    elif warunek3:
        #Kod jest wykonywany tylko wtedy jeżeli warunek jest spełniony a warunek2 nie jest
        pass
    else:
        #Kod jest wykonywany tylko wtedy jeżeli warunek jest spełniony a warunek2 i warunek 3 nie
        pass
else:
    pass

