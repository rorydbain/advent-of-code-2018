from functools import reduce
import re

with open('input.txt') as f:
	content = f.readlines()

content = [line.strip() for line in content]

path_options = {}
nodes_to_dependants = {}
all_dependents = set()
all_dependees = set()

for line in content:
	regex = 'Step ([A-Z])+ must be finished before step ([A-Z]+) can begin\.'
	match = re.match(regex, line, re.I)
	
	if match:
		dependant, dependee = match.groups()
		path_options[dependant] = path_options.get(dependant, set()).union(set(dependee))
		nodes_to_dependants[dependee] = nodes_to_dependants.get(dependee, set()).union(set(dependant))
		all_dependents.add(dependant)
		all_dependees.add(dependee)

starts = all_dependents.difference(all_dependees)
ends = all_dependees.difference(all_dependents)

list_starts = list(starts)
list_starts.sort()

first = list_starts[0]
last = ends.pop()

visits = [first]
options = set(list_starts[1:]) #add the remaining start options

def add_dependees_to_options_if_no_remaining_dependants(dependees):
	for dependee in dependees:
		deps = nodes_to_dependants.get(dependee, set())
		other_dependants = deps.difference(set(visits))
		if not other_dependants:
			options.add(dependee)

add_dependees_to_options_if_no_remaining_dependants(path_options[first])

while options:
	options_as_list = list(options)
	options_as_list.sort()
	current = options_as_list[0]
	visits.append(current)

	add_dependees_to_options_if_no_remaining_dependants(path_options.get(current, []))
		
	options.remove(current)

print(''.join(visits))
	
