import view
import models
import logging


logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG,
                    encoding='utf-8')


def main():
    select = view.show_menu()
    while True:
        if select == 1:
            logging.info('Выбран 1') 
            sotr = models.get_lists()
            view.show_employees(sotr)
            logging.info('Все сработало')
        elif select == 2:
            logging.warning('Выбран 2')
            data = view.add_employees()
            models.add_employee_to_list(data)
            logging.warning('Все сработало')
        elif select == 3:
            logging.info('Выбран 3') 
            models.update_employees(*view.change_employees())
            logging.warning('Все сработало')
        elif select == 4:
            logging.info('Выбран 4') 
            number = view.delete()
            models.delete(number)
            logging.warning('Все сработало')
        elif select == 5:
            logging.info('Выбран 5') 
            view.end()
        elif select == 6:
            logging.info('Выбран 6') 
            models.rewrite(*view.rewrite())
            logging.warning('Все сработало')
        else:
            print('Все пропало!')
        logging.info('Все сработало')
        select = view.show_menu()
