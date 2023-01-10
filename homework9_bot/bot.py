import telebot
import view
import models
import logging


bot = telebot.TeleBot('5915594368:AAEu02qoJXPELmL-C0rCvxA2K541FOhVZz8')


logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG,
                    encoding='utf-8')


@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text == '/start':
        logging.info('Вывод меню команд') 
        view.show_menu(bot, message)
        logging.info('Все сработало')
    elif message.text == '1':
        logging.info('Выбран 1') 
        sotr = models.get_lists()
        view.show_employees(bot, message, sotr)
        logging.info('Все сработало')
    elif message.text[0] == '2':
        logging.warning('Выбран 2')
        data = view.add_employees(bot, message)
        try:
            models.add_employee_to_list(data)
            bot.send_message(message.chat.id, 'Сотрудник успешно добавлен')
            logging.warning('Все сработало')
        except Exception:
            bot.send_message(message.chat.id, 'Что-то пошло не так. Пример ввода: 2: Алексеев Богдан 229 богдан')
        logging.warning('Все сработало')
    elif message.text[0] == '3':
        logging.info('Выбран 3') 
        try:
            models.update_employees(*view.change_employees(bot, message))
            bot.send_message(message.chat.id, 'Сотрудник изменен')
        except IndexError:
            bot.send_message(message.chat.id, 'Сотрудник с таким номером не обнаружен')
        except Exception:
            bot.send_message(message.chat.id, f'Предполагался номер сотрудника, а получен "{message.text.split()[1]}"')
        logging.warning('Все сработало')
        logging.warning('Все сработало')
    elif message.text[0] == '4':
        logging.info('Выбран 4') 
        try:
            number = view.delete(bot, message)
            models.delete(number)
            bot.send_message(message.chat.id, 'Сотрудник удален')
        except IndexError:
            bot.send_message(message.chat.id, 'Сотрудник с таким номером не обнаружен')
        except Exception:
            bot.send_message(message.chat.id, f'Предполагался номер сотрудника, а получен "{message.text.split()[1]}"')
        logging.warning('Все сработало')
    else:
        logging.info('Что-то не так')
        bot.send_message(message.chat.id, 'Неверная команда. /start: список доступных команд')



bot.polling(none_stop=True, interval=0)



    
       
