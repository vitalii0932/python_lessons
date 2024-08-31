import telebot
import random

bot = telebot.TeleBot('')

random_number = random.randint(1, 10)

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Привіт! Я загадав число від 1 до 10. Спробуй його вгадати!')
     

@bot.message_handler(commands=['end'])
def end(message):
    global random_number
    bot.send_message(message.chat.id, f'Нажаль ви програли. Числдом було {random_number}')
    random_number = random.randint(1, 10)


@bot.message_handler(func=lambda message: True)
def guess_function(message):
    global random_number  # Use the global random_number variable

    try:
        # Try to convert the user's message to an integer
        user_guess = int(message.text)

        # Check if the user's guess matches the random number
        if user_guess == random_number:
            # If guessed correctly, send a congratulatory message
            bot.send_message(message.chat.id, f'Молодець! Ти вгадав число: {random_number}')
            # Generate a new random number for the next round
            random_number = random.randint(1, 10)
        elif user_guess < random_number:
            # If the guess is too low, inform the user
            bot.send_message(message.chat.id, 'Ваше число замале')
        else:
            # If the guess is too high, inform the user
            bot.send_message(message.chat.id, 'Ваше число завелике')
    except ValueError:
        # If the user's input is not a valid integer, send a sticker as an error response
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMSZoBGVZULxUT27rXdLav0crVYOYAAAmJHAAKmgchK6_PIQ8usC-o1BA')


if __name__ == '__main__':
	bot.polling(none_stop=True)