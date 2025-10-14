import math
#“Osoba X Y pracuje w naszej firmie od Z lat”.

def powitanie(imie, powtorzenia):
    for i in range(powtorzenia):
        print(f"Hej {imie}")

#powitanie("Adam", 5)

def prostokat(a, b):
    pole = a*b
    print(f"Pole prostokąta o bokach {a}x{b} = {pole}")

prostokat(5,10)
prostokat(2,3)

def kolo(promien):
    pole = 2 * math.pi * promien
    print(f"Pole koła o promieniu {promien} wynosi {pole} ")

kolo(3)
kolo(10)
