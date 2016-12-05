#!/usr/bin/python
class Position:
	numberOfDirection = 4
	def __init__(self, x, y, direction):
		self.x = x
		self.y = y
		self.direction = direction

	def move(self, turn, distance):
		if turn == 'L':
			if self.direction == 0:
				self.direction = self.numberOfDirection-1
			else:
				self.direction -= 1
		elif turn == 'R':
			self.direction = (self.direction + 1) % self.numberOfDirection
		else:
			print 'Error'

		if self.direction == 0:
			self.y += distance
		elif self.direction == 2:
			self.y -= distance
		elif self.direction == 1:
			self.x -= distance
		elif self.direction == 3:
			self.x += distance
		else:
			print 'Error'


data = open('input', 'r')
line = data.readline()
directions = line.split(', ')

myPos = Position(0,0,0)
for value in directions:
	myPos.move(value[0], int(value[1:]))

print str(abs(myPos.x) + abs(myPos.y))

