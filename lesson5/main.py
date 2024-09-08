"""
list = list()
list = [1, 2, 3, 4, 5, 6]

python_list = ['p', 'y', 't', 'h', 'o', 'n']
print(python_list[-3])

matrix = [[[1, 2, 3], 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][0][0])

# task 1
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list)

print('---------------------------')

list.remove(0)
print(list)
list.remove(5)
print(list)
list.remove(7)
print(list)

# task 2
empty = []
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if len(empty) == 0:
	print('Empty')
"""

# task 3
list = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(list)):
	list[i] = list[i] ** 10

list.sort()

print(list)