#!/usr/bin/python
data = open('input', 'r')
possibleTriangles = 0
column0 = []
column1 = []
column2 = []
for line in data:
	values = map(int, line.split())
	column0.append(values[0])
	column1.append(values[1])
	column2.append(values[2])
	if (len(column0) == 3):
		if 2*max(column0) < sum(column0):
			possibleTriangles += 1
		del column0[:]
		if 2*max(column1) < sum(column1):
			possibleTriangles += 1
		del column1[:]
		if 2*max(column2) < sum(column2):
			possibleTriangles += 1
		del column2[:]

print possibleTriangles

