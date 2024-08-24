"""
list1 = ['a', 'b', 'b', 'c', 'c']
print(list1)

list1.append('d')
print(list1)

# list1.clear()
# print(list1)

list1.remove('b')
print(list1)

char = list1.pop(0)
print(char)
print(list1)

del list1[0]
print(list1)

list1.insert(1, 4)
list1.insert(1, 4)
list1.insert(1, 4)
print(list1)

list2 = [-9, 4, 6, -10]
list1.extend(list2)
print(list1)

index = list1.index('c', 1, 7)
print(index)

count = list1.count('a')
print(count)

list2.sort(reverse=True)
print(list2)

list2.reverse()
print(list2)

list1 = [1, 2, 3, 4]
list2 = list1
print(list1)
print(list2)

del list1[0]
print(list1)
print(list2)

a = 6
b = a
a = 3
print(a)
print(b)

list2 = list1.copy()
del list1[0]
print(list1)
print(list2)

print(len(list1))

if 10 in list2:
	print('+')
else:
	print('-')
"""

# task 1
products = ['a', 'b', 'c', 'a', 'b', 'c']
sale_history = []

while True:
	print('1. Всі товари')
	print('2. Додати товар')
	print('3. Придбати товар')
	print('4. Зміна')
	print('5. Історія продажів')
	print('6. Динаміка продажу')

	try:
		operation = int(input('Введіть номер обраної операції: '))

		if operation == 1:
			for product in products:
				print(' -', product)
		elif operation == 2:
			new_product = input('Введіть назву нового продукту: ')
			products.append(new_product)
		elif operation == 3:
			product = input('Введіть назву продуту який хочете придбати: ')
			products.remove(product)
			
			print(f'Ви успішно придбали {product}')

			sale_history.append(product)
		elif operation == 4:
			product = input('Введіть назву продуту який хочете змінити: ')
			index = products.index(product)

			products.remove(product)

			new_product = input('Введіть назву нового продуту: ')
			products.insert(index, new_product)

			print(f'Ви успішно змінили {product} на {new_product}')
		elif operation == 5:
			print('Історія продажу:')
			for item in sale_history:
				print(' -', item)
		elif operation == 6:
			print('Динаміка продажу:')
			reverse_sale_history = sale_history.copy()
			reverse_sale_history.reverse()

			for item in reverse_sale_history:
				print(' -', item)
		else:
			print('Невідома операція')
	except ValueError:
		print('Ви ввели не коректну операцію')