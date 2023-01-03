import csv


lst = []
with open('file.csv', encoding='utf-8') as r_file:
    reader_object = csv.reader(r_file, delimiter=';')
    for row in reader_object:
        lst.append(row)


with open('file1.csv', mode='w', encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=',', lineterminator='\n')
    for row in lst:
        file_writer.writerow(row)


lst1 = []
with open('file.txt', encoding='utf-8') as r_file:
    for row in r_file.readlines():
        lst1.append(row.rstrip('\n'))


with open('file1.txt', mode='w', encoding='utf-8') as w_file:
    for i in range(len(lst1) // 4):
        string = lst1[i * 4 + 0] + ' ' + lst1[i * 4 + 1] + ' ' + lst1[i * 4 + 2] + ' ' + lst1[i * 4 + 3] + '\n'
        w_file.writelines(string)