from functools import reduce
from datetime import datetime, timedelta
import numpy as np
import re

with open('input.txt') as f:
	content = f.readlines()
	
content = [line.strip() for line in content]
content.sort()

def minute_from_timestamp(timestamp):
	up_to_bracket = timestamp.split(']')[0]
	minute_only = up_to_bracket.split(':')[1]
	return int(minute_only)

guard_sleep_schedule = {}
current_guard = None
previous_time = None																

for line in content:
	
	match = re.match('\[[0-9\-]+ [0-9:]+\] Guard #([0-9]+) begins shift', line, re.I)
	minute = minute_from_timestamp(line)
	
	if match:
			
		#set the new current guard
		current_guard = match.groups()[0]
		
	elif 'wakes' in line:
			# presume guard has been awake since the last time stamp, record segment
			existing_time_logs = guard_sleep_schedule.get(current_guard, np.zeros(60))
			existing_time_logs[previous_time:minute] += np.ones(minute - previous_time)
			guard_sleep_schedule[current_guard] = existing_time_logs

	previous_time = minute
			
guards_to_time_asleep = { k: np.sum(v) for k,v in guard_sleep_schedule.items() }
most_asleep_guard = max(guards_to_time_asleep, key=guards_to_time_asleep.get)
print("Most asleep: " + most_asleep_guard)

times = guard_sleep_schedule[most_asleep_guard]
for i, time in np.ndenumerate(times):
	print('{i}: {time}'.format(i=i, time =time))

print("Part 2 ----------")
# Part 2
max_guard_id = None
max = 0
for guard_id, times in guard_sleep_schedule.items():
	most_asleep = np.amax(times)
	if most_asleep > max:
		max_guard_id = guard_id
		max = most_asleep

print("Guard most asleep in any minute is: {guard}".format(guard=max_guard_id))
times = guard_sleep_schedule[max_guard_id]
for i, time in np.ndenumerate(times):
	print('{i}: {time}'.format(i=i, time =time))
