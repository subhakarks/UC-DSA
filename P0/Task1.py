"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
t_nos = set()
for rec in texts:
    t_nos.add(rec[0])
    t_nos.add(rec[1])

for rec in calls:
    t_nos.add(rec[0])
    t_nos.add(rec[1])

print('There are {} different telephone numbers in the records.'.format(len(t_nos)))
