def say_hello(name):
	print(f'Hello, {name}!')
	print('How are you today?')


def calculate(num1, num2, operation):
	if operation == '+':
		return num1 + num2
	elif operation == '-':
		return num1 - num2
	elif operation == '*':
		return num1 * num2
	elif operation == '/':
		if num2 == 0:
			return 'Division by zero'
		return num1 / num2
	else:
		return 'Invalid operation'

x = 10

def print_x():
	global x
	x = 7
	print(x)


def circle_area(radius: float, P = 3.14) -> float: 
	return P * radius ** 2


def test_args_kwargs(*args, **kwargs):
	print(args)
	print(kwargs)


def get_unique_elements(lst):
	return list(set(lst))

def factorial(n):
	if type(n) != int:
		return 'Invalid input'
	if n == 0:
		return 1
	return n * factorial(n - 1)


if __name__ == '__main__':
	names = ['Alice', 'Bob', 'Charlie']
	for name in names:
		say_hello(name)

	num1 = 17
	num2 = 5
	operations = ['+', '-', '*', '/']
	for operation in operations:
		result = calculate(num1, num2, operation)
		print(f'{num1} {operation} {num2} = {result}')

	print(x)
	print_x()
	print(x)

	print(circle_area(6))

	test_args_kwargs(1, 2, 3, 10, 'hi', a = 4, b = 5, c = 6, d = 'hello')