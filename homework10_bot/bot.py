import telebot
import view
import models

bot = telebot.TeleBot('5915594368:AAEu02qoJXPELmL-C0rCvxA2K541FOhVZz8')


@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text == '/start':
        view.show_menu(bot, message)
    elif message.text == 'game':
        view.start(bot, message)
    elif message.text.split()[0] == 'turn':
        view.make_turn(bot, message)
    else:
        view.nevermind(bot, message)


bot.polling(none_stop=True, interval=0)



    
       
