def show_menu(bot, message):
    bot.send_message(message.chat.id, 'Выберите команду: \n "1" - показать всех сотрудников\n "2 name sname phone desc"'
                                      ' - добавить сотрудника\n "3 n name sname phone desc" - изменить данные сотрудника'
                                      ' (n - номер строки)\n "4 n" - удалить сотрудника (n - номер строки)\n ')


def show_employees(bot, message, spisok):
    string = 'Список всех сотрудников: \n'
    for i, sotrudnik in enumerate(spisok):
        if i != 0:
            string += str(i) + ': ' + ' '.join(sotrudnik) + '\n'
    if i == 0:
        string += 'Сотрудников не обнаружено'
    bot.send_message(message.chat.id, string)


    
def add_employees(bot, message):
    data = message.text.split()[1:]
    return data


def change_employees(bot, message):
    change = int(message.text.split()[1])
    string = message.text.split()[2:]
    return change, string


def delete(bot, message):
    number = int(message.text.split()[1])
    return number

def rewrite(bot, message):
    print('Введите название файла, откуда идет запись: ')
    filename1 = input()
    print('Введите название файла, куда идет запись: ')
    filename2 = input()
    return filename1, filename2


def end():
    exit()