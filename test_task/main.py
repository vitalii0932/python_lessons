import telebot
import random

BOT_API_KEY = '7410558573:AAGPjprAMpTdHZuRdfZyiCGpTcQYwzErNYM'

bot = telebot.TeleBot(BOT_API_KEY)

random_number = random.randint(1, 10)

@bot.message_handler(commands = ['start'])
def start(message):
	bot.send_message(message.chat.id, 'Привіт. Я загадав число від 1 до 10. Гра почалась!')

@bot.message_handler(commands = ['end'])
def end(message):
	global random_number

	bot.send_message(message.chat.id, f'Твоїм числом було: {random_number}')

@bot.message_handler(func = lambda message: True)
def guess_function(message):
	global random_number

	try:
		user_guess = int(message.text)

		if user_guess == random_number:
			bot.send_message(message.chat.id, 'Молодець! Ти вгадав число. Я загадав нове число, давай грати далі!')
			random_number = random.randint(1, 10)
		elif user_guess < random_number:
			bot.send_message(message.chat.id, 'Твоє число менше за те, яке було загадано')
		else:
			bot.send_message(message.chat.id, 'Твоє число більше за те, яке було загадано')

	except ValueError:
		bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMSZoBGVZULxUT27rXdLav0crVYOYAAAmJHAAKmgchK6_PIQ8usC-o1BA')
		bot.send_message(message.chat.id, 'Спробуй ще. Тип даних не коректний. Error 500')

if __name__ == '__main__':
	bot.polling(none_stop = True)
