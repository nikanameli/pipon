# Вычислить число c заданной точностью d
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi

n =  input("Введите число для заданной точности числа Пи: ")
p = 0
flag = False
for i in n:
    if flag:
        p +=1
    if i == "." or i == ",":
        flag = True
print(f"Число Пи с заданной точностью {n} равно {round(pi, p)}")