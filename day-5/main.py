import re
from string import ascii_lowercase

with open('input.txt') as f:
	content = f.readlines()[0]

content = content.strip()
print("There are {cout} chars in total".format(cout=len(content)))

def willReact(char_a, char_b):
	return char_a.lower() == char_b.lower() and ((char_a.islower() and char_b.isupper()) or char_a.isupper() and char_b.islower())

def strip_reacting_chars(index, string):
	if index == len(string) - 1:
		return (string, None)
	elif index < 0:
		return (string, index + 1)
	
	current_char = string[index]
	next_char = string[index + 1]
	
	if willReact(current_char, next_char):
		new_string = string[:index] + string[index + 2:]
		return (new_string, index - 1)
	else:
		return (string, index + 1)

def react_text(text):
	stripped, index = strip_reacting_chars(0, text)
	while index is not None:
		stripped, index = strip_reacting_chars(index, stripped)
	return stripped
	
shortest_length = None
for letter in ascii_lowercase:
	regex = '{lower}|{upper}'.format(lower=letter, upper=letter.upper())
	stripped = re.sub(regex, "", content)
	
	reacted = react_text(stripped)
	length = len(reacted)
	
	if shortest_length is not None:
		if length < shortest_length:
			shortest_length = length
	else:
		shortest_length = length

print(shortest_length)			
	
	

