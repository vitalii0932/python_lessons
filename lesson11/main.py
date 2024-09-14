# task 1

"""
user_str = input("Enter a string: ")

repeated_chars_set = {}

for i in range(len(user_str)):
	for j in range(i+1, len(user_str)):
		subs = user_str[i:j]
		remaining_str = user_str[j:]
		if subs in remaining_str and len(subs) > 1:
			repeated_chars_set.add(subs)

print(repeated_chars_set)


# 121 1221 12321 123321 1234321

int = 122
str = str(int)[::-1]
print(str)
"""

import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ_-'

password = ''

length = int(input("Enter the length of the password: "))

while True:
	print('0. Get the password')
	print('1. Add a character')
	print('2. New length')

	operation = input("Enter the operation: ")

	if operation == '0':
		for i in range(length):
			password += random.choice(chars)
		
		chars_size = input("Enter the size of the password: (s/b) ")
		if chars_size == 's':
			print(password)
		elif chars_size == 'b':
			print(password.upper())
		else:
			print("Invalid size")
		password = ''
	if operation == '1':
		new_char = input("Enter a character: ")
		if len(new_char) == 1:
			if not new_char in chars:
				chars += new_char
			else:
				print("The character is already in the list")
		else:
			print("Please enter only one character")
	if operation == '2':
		length = int(input("Enter the length of the password: "))
	
