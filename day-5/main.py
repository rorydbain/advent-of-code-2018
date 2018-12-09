
with open('input.txt') as f:
	content = f.readlines()[0]

content = content.strip()[:980]
print("There are {cout} chars in total".format(cout=len(content)))

def willReact(char_a, char_b):
	return char_a.lower() == char_b.lower() and ((char_a.islower() and char_b.isupper()) or char_a.isupper() and char_b.islower())

def strip_reacting_chars(index, string):
	if index == len(string) - 1:
		return string
	elif index < 0:
		return strip_reacting_chars(index + 1, string)
	
	current_char = string[index]
	next_char = string[index + 1]
	
	if willReact(current_char, next_char):
		new_string = string[:index] + string[index + 2:]
		return strip_reacting_chars(index - 1, new_string)
	else:
		return strip_reacting_chars(index + 1, string)
		
stripped = strip_reacting_chars(0, content)

print(stripped)
print("number of characters:{count}".format(count=len(stripped)))
