wiadomosc = '''
Python lubi zapisywać 
wiadomości do plików
'''
with open("wiadomosc.txt", "w") as plik:
    plik.write(wiadomosc)