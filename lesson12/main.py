"""
my_list = [1, 2, 3, 4, 5]

print(my_list[0])

my_dict = {1: 'one', 2: 'two', 3: 'three'}
my_dict = {'one': 1, 'two': 2, 'three': 3}

print(my_dict['one'])

my_dict['four'] = 4

print(my_dict)

print(my_dict.pop('four'))

print(my_dict)

new_dict = {'three': 6, 'four': 4, 'five': 5}

my_dict.update(new_dict)

print(my_dict)

print(my_dict.keys())

for key in my_dict.keys():
	print(f'for key: {key} value: {my_dict[key]}')

my_dict.clear()

print(my_dict)


months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

date = input('Enter date in format dd.mm.yyyy: ')

date_list = date.split('.')

month = int(date_list[1])

month_name = months[month]

print(f'The month is {month_name}')

month_name.upper()

print(f'The month is {month_name}')
"""

students = {'John': [100, 90, 80], 'Jane': [90, 80, 70], 'Jack': [80, 70, 60]}
students_avg = {}

for student in students.keys():
	marks = students[student]

	total = sum(marks)

	average = total / len(marks)

	students_avg[student] = average

print(students_avg)