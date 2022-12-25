# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

f = open('41.txt','r')
string =  f.readline()
new_string = ""
last_el = string[0]
counter = 1
for el in string[1:]:
    if last_el == el:
        counter +=1
    else:
        new_string += str(counter) + last_el
        counter = 1
    last_el = el
new_string += str(counter) + last_el
f2 = open('42.txt','w')
f2.writelines(new_string)
f.close()
f2.close()
