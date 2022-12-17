# Реализуйте алгоритм перемешивания списка
# (shuffle использовать нельзя, другие методы из библиотеки random - можно).

import random
n = int(input("Введите число эллементов массива: "))
sp = []
for i in range( 1, n + 1):
    sp.append(i)
print(sp)
newsp = random.sample(sp, n)
print(newsp)


