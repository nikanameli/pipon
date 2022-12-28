# В модуле math есть функция math.gcd(a, b), возвращающая наибольший 
# общий делитель (НОД) двух чисел. Вычислите и напечатайте наибольший 
# общий делитель для списка натуральных чисел. Ввод чисел продолжается до ввода пустой строки.
# 36 12 144 18 - 6


import math


print("Введите натуральные числа через Enter: ")
n = input()
sp = []
while n != "":
    sp.append(int(n))
    n = input()
print(sp)
nod = sp[0]
for i in range(len(sp)):
    nod = math.gcd(nod, sp[i])
print(nod)
