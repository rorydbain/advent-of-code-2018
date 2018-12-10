import collections
import numpy as np
from string import ascii_letters

with open('input.txt') as f:
	content = f.readlines()
	
content = [tuple(map(int, f.strip().split(','))) for f in content]


def calculate_distance(x1, y1, x2, y2):
	return abs(x1 - x2) + abs(y1 - y2)
	
grid_size = max(list(sum(content, ()))) + 1

grid = np.chararray([grid_size, grid_size])

letters = {}
for index, val in enumerate(content):
	letters[ascii_letters[index]] = val

for x in range(0, grid_size):
	for y in range(0, grid_size):
		
		letters_to_distance = {}
		for letter, coord in letters.items():
				letters_to_distance[letter] = calculate_distance(coord[0], coord[1], x, y)
		
		closest_letter = min(letters_to_distance, key=letters_to_distance.get)
		closest_letter_distance = letters_to_distance[closest_letter]

		occ = 0
		for letter, distance in letters_to_distance.items():
			if distance == letters_to_distance[closest_letter]:
				occ += 1
		
		if occ == 1:
			grid[x,y] = closest_letter
		elif occ > 1:
			grid[x,y] = None


print("Grid with areas ----------")
print(grid)

counts = collections.Counter(grid.flatten())
print("\n\nWith infite counts --------")
print(counts)

print("\n\nfirst column", grid[:,0])
print("first row", grid[0,:])
print("last column", grid[:,-1])
print("last row", grid[-1,:])
without_infinite = { k: v for k, v in counts.items() if not k in grid[:,0] and not k in grid[0,:] and not k in grid[:,-1] and not k in grid[-1,:] }

print("\n\nWithout infinite counts ------")
print(without_infinite)

largest_area = max(without_infinite, key=without_infinite.get)
print(largest_area, without_infinite[largest_area])
