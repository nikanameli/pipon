# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

n = [int(a) for a in input("Введите последовательность чисел через пробел : ").split()]
sp = []
for i in n:
    if i not in sp:
        sp.append(i)
print(sp)
