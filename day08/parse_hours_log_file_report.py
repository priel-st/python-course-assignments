import re
from datetime import datetime

with open("timelog.txt", "r") as file:
    lines = [line.strip("\n") for line in file]

ranges = []
block = []

for line in lines:
    if line == "":
        for i in range(len(block) - 1):
            match1 = re.search(r'\d{2}:\d{2}', block[i])
            match2 = re.search(r'\d{2}:\d{2}', block[i + 1])
            activity = re.search(r'[A-Za-z ]+', block[i])
            ranges.append((match1.group(0), match2.group(0), activity.group(0).strip()))
        print()
        block = []
    else:
        block.append(line)

for i in range(len(block) - 1):
    match1 = re.search(r'\d{2}:\d{2}', block[i])
    match2 = re.search(r'\d{2}:\d{2}', block[i + 1])
    activity = re.search(r'[A-Za-z ]+', block[i])
    ranges.append((match1.group(0), match2.group(0), activity.group(0).strip()))

for idx, r in enumerate(ranges):
    if r[0] == "09:30" :
        print() 
    print(f"{r[0]}-{r[1]} {r[2]}")

print()

activity_minutes = {}
total_minutes = 0

for r in ranges:
    start = datetime.strptime(r[0], "%H:%M")
    end = datetime.strptime(r[1], "%H:%M")
    minutes = int((end - start).total_seconds() // 60)
    if r[2] not in activity_minutes:
        activity_minutes[r[2]] = minutes
    else:
        activity_minutes[r[2]] += minutes
    total_minutes += minutes

for activity in sorted(activity_minutes):
    mins = activity_minutes[activity]
    percent = round((mins / total_minutes) * 100)
    print(f"{activity:<25}{mins:>4} minutes   {percent:>2}%")
