import utils
import models


def show_menu(bot, message):
    bot.send_message(message.chat.id, 'Попробуй обыграть меня в камешки! Правила простые: есть случайное число камней. Ты можешь взять не более'
                                      '13 камней за ход. Побеждает тот, после хода которого не останется ни одного камня!\n'
                                      'Список команд: game - начать игру (или начать сначала, это автопобеда моя))\n'
                                      'turn <n> - взять n камней (жульничество я не потерплю!!\n')


def start(bot, message):
    user_id = message.chat.id 
    stones = utils.random_stones()
    status = models.start(user_id, stones)
    string = f'Начинаем новую игру с {stones} камнями'
    if status:
        string = 'Опять победа)) Как легко)))\n' + string
    bot.send_message(user_id, string) 
    if utils.robot_first(stones):
        bot.send_message(user_id, 'Пожалуй, схожу первый в этот раз')
        status, second = models.make_turn(user_id, utils.make_turn(stones))
        if status:
            bot.send_message(user_id, f'Я сходил! Осталось {second} камней')
    bot.send_message(user_id, 'Ваш ход')
    return


def make_turn(bot, message):
    user_id = message.chat.id 
    try:
        counts_of_stones = int(message.text.split()[1])
        if counts_of_stones > 13 or counts_of_stones < 1:
            raise Exception
    except Exception:
        bot.send_message(user_id, 'Кажется, вы что-то ввели не так. Число камней должно быть в диапазоне от 1 до 13')
        return
    status, second = models.make_turn(user_id, counts_of_stones)
    if not status:
        if second == 1 or second == 4:
            bot.send_message(user_id, 'Кажется, игра уже закончена или вовсе не начата. Начните игру командой \"game\"')
        elif second == 2:
            bot.send_message(user_id, 'Кажется, вы что-то ввели не так. Число камней должно быть в диапазоне от 1 до 13')
        else:
            bot.send_message(user_id, 'Слишком много камней, осталось меньше. ')
    else:
        if second > 0:
            stones_bot = utils.make_turn(second)
            bot.send_message(user_id, f'Возьму {stones_bot} камней')
            status, second = models.make_turn(user_id, stones_bot)
            if status:
                bot.send_message(user_id, f'Я сходил! Осталось {second} камней')
            if second == 0:
                bot.send_message(user_id, 'Легкая победа))')


def nevermind(bot, message):
    user_id = message.chat.id 
    bot.send_message(user_id, 'а?)')