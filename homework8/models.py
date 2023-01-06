import csv


def get_lists():
    with open('file.csv', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', )
        # tetle = next(reader)
        return list(reader)


def add_employee_to_list(employees):
    with open('file.csv', 'a', encoding='utf8', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(employees)


def update_employees(number, string):
    try:
        with open('file.csv', 'r', encoding='utf8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            data = list(reader )
            data[number] = string
        with open('file.csv', 'w', encoding='utf8', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for row in data:
                if row:
                    writer.writerow(row) 
    except IndexError:
        print('Вы вышли на границу списка.')
        exit
    except Exception:
        print('Ошибка! то-то где-то не так.')
        exit()


def delete(number):
    with open('file.csv', 'r', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = list(reader )
        del data[number]
    with open('file.csv', 'w', encoding='utf8', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for row in data:
            writer.writerow(row) 


def rewrite(file_from, file_to):
    try:
        with open(file_from, 'r', encoding='utf8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            data = list(reader )
        with open(file_to, 'w', encoding='utf8', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for row in data:
                if row:
                    writer.writerow(row)
    except FileNotFoundError:
        print('Не найден один из файлов, которые вы ввели')
