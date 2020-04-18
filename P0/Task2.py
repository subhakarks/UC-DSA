"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
call_recs = dict()
for call in calls:
    duration = int(call[-1])
    call_recs[call[0]] = call_recs.get(call[0], 0) + duration
    call_recs[call[1]] = call_recs.get(call[1], 0) + duration

max_tel = None
max_duration = 0
for k, v in call_recs.items():
    if v > max_duration:
        max_tel = k
        max_duration = v

print('{} spent the longest time, {} seconds, on the phone during Septemeber 2016.'.format(max_tel, max_duration))
