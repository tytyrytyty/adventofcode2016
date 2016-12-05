#!/usr/bin/python
class Position:
	SIZE = 2
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def move(self, direction):
		newX = self.x
		newY = self.y
		if direction == 'U':
			newY += 1
		elif direction == 'D':
			newY -= 1
		elif direction == 'R':
			newX += 1
		elif direction == 'L':
			newX -= 1
		else:
			print 'Error'
		if ((abs(newX) + abs(newY)) <= self.SIZE):
			self.x = newX
			self.y = newY

	def getCode(self):
		if self.y == 0:
			return 7+self.x
		elif self.y == 1:
			return 3+self.x
		elif self.y == 2:
			return 1
		elif self.y == -1:
			return chr(ord('B') + self.x)
		elif self.y == -2:
			return 'D'


data = open('input', 'r')
myPos = Position(-2,0)
for line in data:
	for direction in line :
		if direction == '\n': continue
		myPos.move(direction)
	print myPos.getCode();



