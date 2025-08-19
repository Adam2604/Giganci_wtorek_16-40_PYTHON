import random

los = random.randint(1, 100) # może być liczba 100
los2 = random.randrange(1, 100) # nie może być liczba 100
los3 = random.random() # liczba pomiędzy 0 a 1
print(los)
print(los2)
print(los3)

print(f"Twoja wylosowana liczba to: {los}")
