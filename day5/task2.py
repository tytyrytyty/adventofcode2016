#!/bin/usr/python

import sys
import hashlib


passwd = list('XXXXXXXX')
nDiscovered = 0
for id in range(30000000):
	h = hashlib.md5( 'ojvtpuvg' + str(id) ).hexdigest()
	if (h[:5]) == '00000':
		position = int(h[5], 16)
		if position >= 0 and position <= 7 and passwd[position] == 'X':
			passwd[position] = h[6]
			nDiscovered += 1
			if nDiscovered == 8:
				break;

print ''.join(passwd)


# 5bfe69