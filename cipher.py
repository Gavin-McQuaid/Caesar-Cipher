import sys
import string
def one_letter_words(w):
	one_letter = ['A','I'] + list(string.digits)
	if w in one_letter:
		return True
	return False

def two_letter_words(w):
	most_common_words = [	
'OF', 'TO', 'IN', 'IT', 'IS', 'BE', 'AS', 'AT', 'SO', 'WE', 'HE', 'BY', 'OR', 'ON', 'DO', 'IF', 'ME', 'MY', 'UP', 'AN', 'GO', 'NO', 'US', 'AM'
 ]
	if w in most_common_words:
		return True
	return False
def has_vowel(w):
	vowels = ['A','E','I','O','U','Y']
	for char in w:
		if char in vowels:
			return True
	return False


lines = []
for line in sys.stdin:
	lines.append(line)


list_of_chars = list(string.ascii_uppercase + string.digits)

d = {}
for i in range(0,len(list_of_chars)):
	d[list_of_chars[i]] = i
j = 0
while j < 37:
	new_lines = []
	copy = list_of_chars
	copy = copy[j:] + copy[:j]
	for line in lines:
		new_line = ''
		for char in line:
			if char in d:
				
				new_line += copy[d[char]]
			else:
				new_line += char
		new_lines.append(new_line)
	copy_lines = []
	for line in new_lines:
		line = line.split()
		words = []
		for word in line:
			if not word.isalnum():
				words.append(word)
			elif word.isnumeric():
				words.append(word)
			elif len(word) == 1 and one_letter_words(word):
				words.append(word)
			elif len(word) == 2 and (two_letter_words(word) or has_vowel(word)):
				words.append(word)
			elif has_vowel(word):
				words.append(word)

		
		if words == line:
			copy_lines.append(' '.join(line))
	if len(copy_lines) >= (len(new_lines) * (4/5)):
		for line in new_lines:
			print(line.strip())

	j += 1
