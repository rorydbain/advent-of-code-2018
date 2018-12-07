import operator
import itertools
from difflib import SequenceMatcher
from collections import Counter
from functools import reduce

with open('input.txt') as f:
	content = f.readlines()

content = [line.strip() for line in content]

total = {"two": 0, "three": 0} 
def addForNumCharacters(val):
	counter = Counter(val.strip())
	hasTwo = 2 in counter.values()
	hasThree = 3 in counter.values()
	
	if hasTwo:
		total["two"] += 1
	if hasThree:
		total["three"] += 1

#for line in content:
#	addForNumCharacters(line)
#print(total["two"] * total["three"])

class MatchedCodes (object):
	def __init__(self, string1, string2, ratio):
		self.string1 = string1
		self.string2 = string2
		self.ratio = ratio
	
	def __str__(self):
		return self.string1 + "-" + self.string2
					
most_similar = None
for (a, b) in itertools.combinations(content,2):
	ratio = SequenceMatcher(None, a, b).ratio()
	if most_similar is None:
		most_similar = MatchedCodes(a, b, ratio)
	elif ratio > most_similar.ratio:
		most_similar = MatchedCodes(a, b, ratio)
	
print(most_similar)

