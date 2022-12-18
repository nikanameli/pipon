# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
n = int(input("Введите число эллементов массива: "))
sp = []
for i in range( 1, n + 1):
    sp.append(round(random.random() * 10, 2))
print(sp)
sp1 = []
for i in range(n):
    sp1.append(round(sp[i] - int(sp[i]), 2))
print(sp1)
print(max(sp1) - min(sp1))