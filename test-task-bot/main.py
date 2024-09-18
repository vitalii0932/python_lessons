import telebot
import random

BOT_API_TOKEN = '7422631432:AAFBO8gi_svzIS6Sii_J1QNAv8Ba2hVFWKc'

bot = telebot.TeleBot(BOT_API_TOKEN)

random_number = random.randint(1, 1000)


@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Привіт! Я загадав число від 1 до 1000. Спробуй відгадати! =)')


@bot.message_handler(func=lambda message: True)
def guess_function(message):
    global random_number

    try:
        number = int(message.text)

        if number == random_number:
            bot.send_message(message.chat.id, 'Вітаю! Ти відгадав число!')
            random_number = random.randint(1, 1000)
        elif number > random_number:
            bot.send_message(message.chat.id, 'Спробуй менше число!')
        else:
            bot.send_message(message.chat.id, 'Спробуй більше число!')
    except ValueError:
        bot.send_message(message.chat.id, 'Введіть число!')


if __name__ == '__main__':
    bot.polling(none_stop=True)