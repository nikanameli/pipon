def show_menu():
    print('Выберите команду: \n 1 - показать всех сотрудников\n 2 - добавить сотрудника\n 3 - изменить данные сотрудника\n 4 - удалить сотрудника\n 5 - завершить работу\n 6 - дублировать данные в другой файл')
    try:
        select = int(input()) 
        if not select in [1, 2, 3, 4, 5, 6]:
            raise ValueError
        return select 
    except Exception: 
        print("Ошибка в вводе команды.")
        show_menu()


def show_employees(spisok):
    print('Список всех сотрудников: ')
    for i, sotrudnik in enumerate(spisok):
        if i == 0:
            print(' ', *sotrudnik)
        else:
            print(i, *sotrudnik)

    
def add_employees():
    print('Введите ФИО, телефон и должность через пробел: ')
    data = input().split()
    return data


def change_employees():
    print('Выберите строку для изменения: ')
    change = int(input())
    print('Выберите строку для записи: ')
    string = input().split()
    return change, string


def delete():
    print('Введите номер строки для удаления: ')
    number = int(input())
    return number

def rewrite():
    print('Введите название файла, откуда идет запись: ')
    filename1 = input()
    print('Введите название файла, куда идет запись: ')
    filename2 = input()
    return filename1, filename2


def end():
    exit()