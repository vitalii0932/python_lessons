def is_anagram(str1: str, str2: str) -> bool:
	if len(str1) != len(str2):
		return False

	return sorted(str1) == sorted(str2)


def main():
	str1 = 'listen'
	str2 = 'false'

	print(is_anagram(str1, str2))


if __name__ == '__main__':
	main()


"""
game

1. Create a new hero with the name and stats
2. Create a tasks for the hero
3. Show results
"""