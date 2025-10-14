from math import sqrt

def pole_szesciokata(a):
    return (3 * sqrt(3) * a ** 2) / 2

pole = pole_szesciokata(10)
pole2 = pole_szesciokata(15)
pole3 = pole_szesciokata(3)

print(pole)
print(pole2)
print(pole3)