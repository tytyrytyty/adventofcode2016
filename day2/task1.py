#!/usr/bin/python
class Position:
	SIZE = 2
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def move(self, direction):

		if direction == 'U':
			if self.y != self.SIZE:
				self.y += 1
		elif direction == 'D':
			if self.y != 0:
				self.y -= 1
		elif direction == 'R':
			if self.x != self.SIZE:
				self.x += 1
		elif direction == 'L':
			if self.x != 0:
				self.x -= 1
		else:
			print 'Error'
	def getCode(self):
		return ((self.SIZE-self.y)*3) + self.x+1


data = open('input', 'r')
myPos = Position(1,1)
for line in data:
	for direction in line :
		if direction == '\n': continue
		myPos.move(direction)
	print myPos.getCode();



