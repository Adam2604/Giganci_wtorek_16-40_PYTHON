'''
Napisz program, który powie Ci czy dany uczestnik może skorzystać z nowej

atrakcji. Ograniczenia:
-minimalny akceptowalny wiek to 12 lat
-minimalny akceptowalny wzrost to 130 cm
-maksymalny akceptowalny wzrost to 195 cm

Program zapyta użytkownika o jego wiek i wzrost, a następnie wyświetli komunikat,
czy wolno mu skorzystać z atrakcji.'''

wiek = int(input("Podaj swój wiek: "))
wzrost = int(input("Podaj swój wzrost: "))

if wiek >= 12 and 130 <= wzrost <= 195:
    print("Wolno ci skorzystać z atrakcji")
else:
    print("Nie wolno ci skorzystać z atrakcji")