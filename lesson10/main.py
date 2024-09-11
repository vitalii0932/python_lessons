"""
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list[0:9:3])\


full_name = input('Input your full name: ')
full_name = full_name.strip()

if ' ' in full_name:
	first_name = full_name[:full_name.index(' ')]
	last_name = full_name[full_name.index(' ') + 1:]

	print(f'Your first name is {first_name} and your last is {last_name}')
else:
	print('Incorrect full name format')


list = ['a', 'b', 'c', 'a']
print(list)

my_set = set('abca')
my_set = {'a', 'b', 'c', 'a'}

my_set.add('d')
my_set.add('d')

print(my_set)

my_set.remove('a')

print(my_set)

my_set.discard('b')

print(my_set)


set1 = set('hello')
set2 = set('have a nice day!')

print(set1.union(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))
"""

import random
list = [random.randint(1, 5000) for i in range(50)]
list.sort()
print(list)

my_set = set(list)

print(list(my_set))