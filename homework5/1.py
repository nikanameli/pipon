# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

n = [str(a) for a in input("Введите слова через пробел : ").split()]
# print(n)
sp = []
for i in n:
        sp.append(i)
# print(sp)


sp = list(filter(lambda x: "абв" not in x,sp))
print(sp)