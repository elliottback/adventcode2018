import re
from collections import Counter
import operator

f = open( "input", "r")

contents = f.read()
lines = contents.split("\n")
lines.sort()

guards = {}
guards_minutes = {}
id = start = end = None

for line in lines:
    if( "Guard" in line ):
        id = start = end = None
        matches = re.match(r"^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}\] Guard #(\d+)", line )
        id = matches.group(1)
    elif "falls asleep" in line:
        matches = re.match(r"^\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})\]", line )
        start = int(matches.group(1))
    elif "wakes up" in line:
        matches = re.match(r"^\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})\]", line )
        end = int(matches.group(1))

        if id not in guards:
            guards[ id ] = 0
        guards[ id ] = guards[ id ] + (end - start)

        if id not in guards_minutes:
            guards_minutes [ id ] = {}

        for min in range(start, end):
            if min not in guards_minutes[ id ]:
                guards_minutes[ id ][ min ] = 0
            guards_minutes[id][min] += 1

# find sleepiest dude
max = 0
maxguard = 0
maxminute = 0

for guard, minutes in guards_minutes.items():
    for minute, minutecount in minutes.items():
        if( minutecount > max):
            maxguard = guard
            max = minutecount
            maxminute = minute

print(maxguard, " - ", maxminute, " = ", int( maxguard ) * int( maxminute ))
exit(0)