#task 1
"""
num = int(input('Please input your number: '))

if num > 0:
	print('+')
elif num < 0:
	print('-')
else:
	print('zero')

#task 2
money = None
if money:
	print("All right!")
else:
	print(":(")

#task 3
user_name = input("Enter your name: ")

if user_name:
	print(f"Hello {user_name}")
else:
	print("Hi Anonym!")

#task 4
name = 'Vitalii'
age = 20
has_driver_licence = False

if age > 18 and has_driver_licence:
	print(f"{name} can drive a car")
else:
	print(f"{name} can`t drive a car")

#task 5
is_nice = False
state = "nice" if is_nice else "not nice"
print(state)

a = 6
b = 10
c = a if a > b else b

#task 6
x = 6
y = 0

if x > 0:
	if y > 0:
		print('I')
	elif y < 0:
		print('IV')
	else:
		print('y = 0')
elif x < 0:
	if y > 0:
		print('II')
	elif y < 0:
		print('III')
	else:
		print('y = 0')
else:
	print('x = 0')
"""

# Завдання щоб повторити та розібратися:
# task 1
"""
Арифметичні дії над числами пронумеровані таким чином: 1 — додавання, 2 — віднімання, 3 — множення, 4 — ділення. Дано номер дії N (ціле число в діапазоні 1–4) та дійсні числа A та B (B не дорівнює 0). Виконати над числами вказану дію та вивести результат.
"""

oper = int(input('Select oper (1 -> + ; 2 -> - ; 3 -> * ; 4 -> /): ')) # ввід користувачем обраної операції
a = float(input('a = ')) # ввід користувачем першого числа 
b = float(input('b = ')) # ввід користувачем другого числа

if oper == 1:  # якщо користувач обрав першу операцію
	print(f'a + b = {a + b}')
elif oper == 2:  # якщо користувач обрав другу операцію
	print(f'a - b = {a - b}')
elif oper == 3:  # якщо користувач обрав третю операцію
	print(f'a * b = {a * b}')
elif oper == 4:  # якщо користувач обрав четверту операцію
	if b == 0:  # якщо користувач другим числом ввів 0 то буде ділення на 0
		print('Divide by zero')
	else:
		print(f'a / b = {a / b}')
else:   # якщо користувач обрав неіснуючу операцію
	print('Unknown oper')

# task 2
"""
Дано ціле число, що лежить у діапазоні 1-999. Вивести рядок-опис виду «парне двозначне число», «непарне тризначне число» тощо.
"""

number = int(input('input your number: ')) # ввід числа користувачем

if number > 0 and number < 1000: # перпевірка на правильність діапазону
	number_desc = 'Число: ' # змінна де буде зберігатися опис числа

	if number % 2 == 0:  # якщо парне (немає остачі від ділення на 2) то додати в опис відповідну позначку 
		number_desc += 'парне '
	else:  # якщо не парне (є остача від ділення на 2) то додати в опис відповідну позначку 
		number_desc += 'не парне '

	if number < 10:  # якщо число від 0 до 9
		number_desc += 'однозначне'
	if number < 100:  # якщо число від 10 до 99
		number_desc += 'двозначне'
	if number < 1000:  # якщо число від 100 до 999
		number_desc += 'тризначне'

	print(number_desc)
else:
	print('Неправильний діапазон')