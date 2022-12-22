# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


k = int(input("Введите натуральную степень k: "))
res = ''
while (k >= 0):
    num = randint(0, 50)
    if num != 0:
        if k > 1:
            res += str(num) + f'x^{k}' + ' + '
        elif k == 1:
            res += str(num) + f'x' + ' + '
        else:
            res += str(num)
    k -= 1
print(f'{res} = 0')

f = open('4py.txt','w')
f.write(f'{res} = 0')
f.close()
