#!/bin/usr/python

import sys
import hashlib


passwd = ''
for id in range(20000000):
	h = hashlib.md5( 'ojvtpuvg' + str(id) ).hexdigest()
	if (h[:5]) == '00000':
		passwd += h[5]
		if len(passwd) == 8:
			break;

print passwd


# 5bfe69