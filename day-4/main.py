from functools import reduce
from datetime import datetime, timedelta
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
		# add awake time for previous guard
		if current_guard and previous_time:
			existing_time_logs = guard_sleep_schedule.get(current_guard, [])
			one_minute_before = minute_earlier(current_timestamp)
			previous_guard_range = (previous_time, one_minute_before)
			guard_sleep_schedule[current_guard] = existing_time_logs + [previous_guard_range]
			
		#set the new current guard
		current_guard = match.groups()[0]
		
	elif 'falls' in line:
			# presume guard has been awake since the last time stamp, record segment
			existing_time_logs = guard_sleep_schedule.get(current_guard, [])
			one_minute_before = minute_earlier(current_timestamp)
			current_guard_range = (previous_time, one_minute_before)
			guard_sleep_schedule[current_guard] = existing_time_logs + [current_guard_range]
			
	previous_time = current_timestamp
			
guards_to_time_awake = { k: time_awake_from_timestamp_tuples(v) for k, v in guard_sleep_schedule.items() }

guard = max(guards_to_time_awake, key=guards_to_time_awake.get)
print(guards_to_time_awake[guard])
