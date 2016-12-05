#!/usr/bin/python
data = open('input', 'r')
possibleTriangles = 0

for line in data:
	values = map(int, line.split())

	if 2*max(values) < sum(values):
		possibleTriangles += 1

print possibleTriangles

