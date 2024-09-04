"""
string = "м'яч"

string = """"""
At ipsum voluptua ea et feugiat. Blandit consetetur magna sed duis ea tempor sea option et te sea tincidunt vero aliquyam. Amet dolores est rebum sed ea iriure dolore autem. Sea in sea kasd amet amet rebum amet eros eirmod ad. Justo consetetur accusam ipsum duis vero nulla gubergren dolore sadipscing erat et. Ut gubergren rebum sadipscing et. Et ea et est. Sit nonumy eros et at hendrerit sit zzril sea accusam ipsum nonummy elitr eirmod dolor justo vero invidunt. Labore consetetur duo dolor eum labore et nulla in dolore dolores ipsum diam est voluptua ut elitr. Sea ea velit sadipscing autem ea odio erat lorem accusam eirmod dolor ex voluptua. Dolor accusam est. Eirmod rebum dolore nihil. Sed labore quis vero nibh nibh odio ipsum eu eirmod dolor accusam enim elitr nulla soluta nulla erat justo. In invidunt magna elitr justo accusam et amet dolor lorem labore erat duo liber sed rebum invidunt sed. Iusto labore dolor et stet. Sea aliquip facilisis consetetur lorem at ut rebum nisl zzril est dolore duo lorem eos. Aliquyam labore at lorem duo tempor no nulla et rebum dolor invidunt magna euismod invidunt. Lorem aliquyam kasd eirmod assum takimata odio erat et amet duo nonumy vero.
""""""

print(string)

one_line_text = "Textual data in Python is handled with str objects, or strings. "\
           	"Strings are immutable sequences of Unicode code points. "\
           	"String literals are written in a variety of ways."

print(one_line_text)


test_str = 'ABCDEFGH'
print(test_str[:-1])

konk = 'Hello' + ' world!'
repl = 'abc' * 10
konk_plus_repl = ('abc_' + 'cba ') * 3

print(konk, repl, konk_plus_repl)


loren_ipsum = 'At ipsum voluptua ea et feugiat. \n\t\v\f\rBlandit consetetur magna sed duis ea tempor sea option et te sea tincidunt vero aliquyam'

print(loren_ipsum)

test_str = 'abcd'
for letter in test_str:
	print(letter)
"""

# task 1
test_string = 'abcba'
is_palindrome = True

for index in range(len(test_string) // 2):
	l = index
	r = - index - 1

	if not test_string[l] == test_string[r]:	
		is_palindrome = False
		break

print(is_palindrome)