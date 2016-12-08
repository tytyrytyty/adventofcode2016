import sys
from collections import Counter

numberofLetters = 8
data = open('input', 'r')

counters = list()
for i in range(numberofLetters):
	counters.append(Counter())

for line in data:
	for i in range(numberofLetters):
		counters[i].update(line[i])

for i in range(numberofLetters):
	sys.stdout.write(str(counters[i].most_common(1)[0][0]))


