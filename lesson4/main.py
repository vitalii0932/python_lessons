"""
# about list
list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]

print(list)

print(list[0])

print(list[len(list) - 1])

list.append(11)

print(list)

# about for and list

for el in list:
	print(el)

fruit = 'apple'
for char in fruit:
	print(char)

colors = ['red', 'green', 'blue', 'yellow']
for color in colors:
	if color == 'blue':
		break

	print(color)


# about for with range() and for in for

for i in range(10):
	print('hi')

matrix = [[1, 2, 3], 
		  [4, 5, 6], 
		  [7, 8, 9]]

for i in matrix:
	for j in i:
		print(j) 



# about while		

a = 1

while a < 5:
	print(a)
	a += 1
else:
	print('a = ', a)

a = 0

while True:
	if a == 10:
		print('The end')
		break

	a += 2

	print(a)


a = 0
while a < 10:
	a += 1

	if a % 2 == 0:
		continue

	print(a)




# task 1
name = input('Please input your name: ')

while not name or name == '':
	name = input('Please input your name: ')

print(f'Hello {name}')



# task 2
word = input('Input your word: ')

while not word:
	word = input('Input your word: ')

char = input('Input your char: ')

while not char or len(char) != 1:
	char = input('Input your char: ')

count = 0

for i in word:
	if i == char:
		count += 1

print(count)
"""