import telebot
import random

BOT_API_KEY = '7346104914:AAFx0Vx_oPX6VdDGllPOpX2rnf1twCaQDeQ'

bot = telebot.TeleBot(BOT_API_KEY)

random_number = random.randint(1, 10)

@bot.message_handler(commands=['start'])
def start(message):
	global random_number
	random_number = random.randint(1, 10)
	bot.send_message(message.chat.id, 'Привіт! Я загадав число від 1 до 10. Спробуй його вгадати!')

@bot.message_handler(commands=['end'])
def end(message):
	global random_number
	bot.send_message(message.chat.id, f'Числом було: {random_number}')
	random_number = random.randint(1, 10)

@bot.message_handler(func=lambda message: True)
def guess_function(message):
	global random_number

	try:
		user_guess = int(message.text)

		if user_guess == random_number:
			bot.send_message(message.chat.id, f'Чудово! Ти вгадав число {random_number}. Давай грати ще!')
			random_number = random.randint(1, 10)
		elif user_guess < random_number:
			bot.send_message(message.chat.id, f'Ваше число {user_guess} замале. Спробуй ще!')
		else:
			bot.send_message(message.chat.id, f'Ваше число {user_guess} завелике. Спробуй ще!')
	except ValueError:
		bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMSZoBGVZULxUT27rXdLav0crVYOYAAAmJHAAKmgchK6_PIQ8usC-o1BA')

if __name__ == '__main__':
	bot.polling(none_stop=True)

print('Hello world!')