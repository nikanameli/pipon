# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
n = int(input("Введите количетво элементов: "))
sp = []
summ = 0
for i in range(0, n):
    sp.append(random.randint(0, 10))
print(sp)
sp1 = []
for i in range (0, round(n / 2 + 0.5)):
    sp1.append(sp[i] * sp[-i - 1])
print(sp1)
