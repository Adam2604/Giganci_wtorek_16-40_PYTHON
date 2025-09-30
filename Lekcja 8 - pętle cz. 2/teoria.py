# 0, 1, 2, 3, 4
range(5)
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
range(10)
# 5, 6, 7, 8, 9, 10, 11, 12
range(5,13)
# -5, -4, -3
range(-5,-2)
# 2, 4, 6, 8, 10
range(2,11,2)
# 0, 5, 10, 15
range(0,16,5)
# -9 -6 -3 0 3
range(-9,4,3)
# -100 -25 50 125
range(-100,126,75)

# for a in range(5):
#     print(f"a = {a}")
#     for b in range(20, 70, 10):
#         print(f"\tb = {b}")
#         pass # for b
#     pass # for a


liczba = int(input("Podaj liczbe: "))
for a in range(liczba):
    print(f'a={a}')
    if a > 4:
        break
    pass
else:
    print("Pętla for wykonałą się bez instrukcji break")
    pass