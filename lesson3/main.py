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
"""

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