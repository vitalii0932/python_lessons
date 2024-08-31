import os

"""
# home task 2
list = ['Анастасія Юріївна', 'Аліна Юріївна', 'Анастасія Михайлівна']

count = 0

for item in list:
	if 'Анастасія' in item:
		count += 1

print(count)


# task1
list1 = []
list2 = []

while True:
	user_input = input('Введіть будь-яке число (для зупинки напишіть stop): ')

	if user_input.lower() == 'stop': 
		break

	try:
		list1.append(int(user_input))
	except ValueError:
		print('Ви ввели не число')

print('Перший список: \n', list1)

for item in list1:
	if not item % 2 == 0:
		list2.append(item)

print('Другий список: \n', list2)
"""

# task 2
to_do_list = []

while True:
	print('0. Show tasks')
	print('1. Add task to list')
	print('2. Remove task from list')
	print('3. Sort tasks')
	print('4. Shut down the program')

	try:
		operation = int(input('Select the operation: '))

		if operation == 0:
			print('Tasks:')
			for i in range(len(to_do_list)):
				print(f'{i}. {to_do_list[i]}')
		elif operation == 1:
			while True:
				new_task = input('Input your task for this day: ')

				if new_task.lower().strip() == 'stop':
					break

				to_do_list.append(new_task)

			os.system('cls')
		elif operation == 2:
			item_to_remove_index = int(input('Input item for remove index: '))

			to_do_list.pop(item_to_remove_index)
		elif operation == 3:
			to_do_list.sort()

			print('List was sorted')
		elif operation == 4:
			break
		else:
			print('Incorrect operation')
	except Exception:
		print('500')

	

