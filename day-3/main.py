import re
import numpy as np

with open('input.txt') as f:
	content = f.readlines()

content = [line.strip() for line in content]

class Box:
	def __init__(self, id, left, top, width, height):
		self.id = id
		self.left = left
		self.top = top
		self.width = width
		self.height = height
	
	def __repr__(self):
		return 'Box {id}: {left},{top}. {width},{height}'.format(id=self.id, left=self.left, top=self.top, width=self.width, height=self.height)
		
	def max_x(self):
		return self.left + self.width
		
	def max_y(self):
		return self.top + self.height
		
	def intersects(self, other_box):
		top_right_x = self.left
		return not (self.max_x() < other_box.left or self.left > other_box.max_x() or self.max_y() < other_box.top or self.top > other_box.max_y())

boxes = []
max_x = 0
max_y = 0

for square_info in content:
	match = re.match('#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)', square_info, re.I)
	if match:
		groups = map(int, match.groups())
		box = Box(*groups)
		max_x = max(box.max_x(), max_x)
		max_y = max(box.max_y(), max_y)
		boxes.append(box)
	else:
		print("failed to parse", square_info)
		
grid = np.zeros((max_x, max_y))

unique_cuts = set([])
for box in boxes:
	x1 = box.left
	x2 = box.max_x()
	y1 = box.top
	y2 = box.max_y()
	if not np.any(grid[x1:x2,y1:y2]):
		unique_cuts.add(box)
	else:
		unique_cuts = set([b for b in unique_cuts if not b.intersects(box)])
	grid[x1:x2,y1:y2] += np.ones((box.width, box.height))

# Part 1
count = (grid >= 2).sum() 
print("Number with more than two is {count}".format(count=count))	
	
# Part 2
for cut in unique_cuts:
	print("The unique cut is {cut}".format(cut=cut))


