from functools import reduce
from datetime import datetime, timedelta
import numpy as np
import re

with open('input.txt') as f:
	content = f.readlines()
	
content = [line.strip() for line in content]
content.sort()
	
def date_from_guard_log(timestring):
	time = timestring.split(']')[0]
	return datetime.strptime(time, '[%Y-%m-%d %H:%M')
	
def minute_earlier(timestamp):
	return timestamp - timedelta(minutes=1)
	
def time_awake_from_timestamp_tuples(time_groups):
	return reduce(lambda total, times: total + (times[1] - times[0]), time_groups, timedelta(0))

guard_sleep_schedule = {}
current_guard = None
previous_time = None	
			
for line in content:
	current_timestamp = date_from_guard_log(line)
	
	match = re.match('\[[0-9\-]+ [0-9:]+\] Guard #([0-9]+) begins shift', line, re.I)
	
	if match:
			
		#set the new current guard
		current_guard = match.groups()[0]
		
	elif 'wakes' in line:
			# presume guard has been awake since the last time stamp, record segment
			existing_time_logs = guard_sleep_schedule.get(current_guard, [])
			one_minute_before = minute_earlier(current_timestamp)
			current_guard_range = (previous_time, one_minute_before)
			guard_sleep_schedule[current_guard] = existing_time_logs + [current_guard_range]
			
	previous_time = current_timestamp
			
guards_to_time_awake = { k: time_awake_from_timestamp_tuples(v) for k, v in guard_sleep_schedule.items() }

most_asleep_guard_id = max(guards_to_time_awake, key=guards_to_time_awake.get)
print("Guard id:{guard}".format(guard=most_asleep_guard_id))
print("Time awake:{asleep}".format(asleep=most_asleep_guard_id))
times_asleep = guard_sleep_schedule[most_asleep_guard_id]

times = np.zeros(60)
print("Times")
for time in times_asleep:
	earlier = time[0].minute
	later = time[1].minute
	times[earlier:later] += np.ones(later - earlier)

for i, time in np.ndenumerate(times):
	print('{i}: {time}'.format(i=i, time =time))


