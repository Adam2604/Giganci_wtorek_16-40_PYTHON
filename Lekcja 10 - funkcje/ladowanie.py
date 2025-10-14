import time

def pasek_ladowania(gotowe, wszystko=100):
    #Znak "#" - oznacza wykonaną część
    #Znak "-" - oznacza niewykonaną część

    wykonane = round(10 * gotowe / wszystko)
    niewykonane = 10 - wykonane

    tekst_wykonane = "#" * wykonane
    tekst_niewykonane = "-" * niewykonane

    print(f"\r[{tekst_wykonane}{tekst_niewykonane}]", end = " ")

for i in range(200):
    pasek_ladowania(i, 200)
    time.sleep(0.1)

