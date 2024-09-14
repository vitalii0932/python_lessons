import telebot
import random

bot = telebot.TeleBot('token')

random_number = random.randint(1, 10)


@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Привіт! Я загадав число від 1 до 10. Спробуй його вгадати!')
     

@bot.message_handler(commands=['end'])
def end(message):
    global random_number 
    
    bot.send_message(message.chat.id, f'Нажаль ви програли. Числом було {random_number}')

    random_number = random.randint(1, 10)


@bot.message_handler(func=lambda message: True)
def guess_function(message):
    global random_number 

    try:
        user_guess = int(message.text)

        if 0 <= user_guess <= 10:
            if user_guess == random_number:
                bot.send_message(message.chat.id, f'Вітаю! Ви вгадали число {random_number}')
                random_number = random.randint(1, 10)
            elif user_guess < random_number:
                bot.send_message(message.chat.id, 'Ваше число замале')
            else:
                bot.send_message(message.chat.id, 'Ваше число завелике') 
        else:
            bot.send_message(message.chat.id, 'Будьте уважні. Ваше число має бути в межах від 1 до 10') 
    except ValueError:
        bot.send_message(message.chat.id, 'Ви ввели не число')


if __name__ == '__main__':
	bot.polling(none_stop=True)