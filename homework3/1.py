# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random


n = int(input("Введите количетво элементов: "))
sp = []
summ = 0
for i in range(0, n):
    sp.append(random.randint(0, 10))
print(sp)
for i in range(1, n, 2):
    summ = summ + sp[i]
print(summ)