#!/bin/usr/python

import sys
from collections import Counter


data = open('input', 'r')

goodSectorsIds = 0
for line in data:
	elements = line.split('-')
	checksum = elements[-1]
	sectorId = int(checksum[:checksum.find('[')])
	checksum = checksum[checksum.find('[')+1:checksum.find(']')]
	del elements[-1]

	counter = Counter()
	for element in elements:
		counter.update(element)

	sortedVals = [x[0] for x in sorted(counter.items(), key=lambda t: (-t[1], t[0]))]
	if ''.join(sortedVals[:len(checksum)]) == checksum:
		goodSectorsIds += sectorId
	


print goodSectorsIds