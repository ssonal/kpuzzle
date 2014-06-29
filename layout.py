from __future__ import print_function
from random import randint,sample,seed
from copy import deepcopy
import keypress

# seed(10299)

class Board(object):

	#map for directions of movement
	__dirs = {
        keypress.UP:      (1,0),
        keypress.DOWN:    (-1,0),
        keypress.LEFT:    (0,1),
        keypress.RIGHT:   (0,-1),
        keypress.UP1:      (1,0),
        keypress.DOWN1:    (-1,0),
        keypress.LEFT1:    (0,1),
        keypress.RIGHT1:   (0,-1),
    }

      #   1
      # 3   4
      #   2

	def __init__(self,size=3,count=34,other=None, **kws):
		self.size = size
		self.board = {}
		self.space = ()
		self.count = count
		self.solution = self.getNewBoard()
		if other:
			self.dict = deepcopy(other.__dict__)


	def getSize(self):
		return self.size

	#Initialization funtion. Creates a new k-puzzle board randomly
	def getNewBoard(self):
		nums = range(1,self.size**2)
		nums += [0]

		b = {}
		k=0
		for i in range(self.size):
			for j in range(self.size):
				b[i,j] = nums[k]
				k+=1

		self.board = deepcopy(b)
		self.space = (self.size-1, self.size-1)
		self.shuffle()
		return b

	def shuffle(self):

		for _ in range(self.count):
			valid_moves = self.getMoves()
			# print(valid_moves)
			move = sample(valid_moves, 1)[0]
			# print (move)
			self.makeMove(move)

	def makeMove(self,dire):
		direction = self.__dirs.get(dire)
		if self.valid(*direction):
			direction = (self.space[0]+direction[0],self.space[1]+direction[1])
			self.board[self.space] = self.board[direction]
			self.board[direction] = 0
			self.space = direction
			return True

		return False


	def getMoves(self):
		moves = [72,80,77,75]

		for move in moves:
			if not self.valid(*self.__dirs.get(move)):
				moves.remove(move)

		return moves


	def getCell(self, i, j):
		return self.board[i,j]

	def getSoln(self):
		return self.solution

	def won(self):
		return self.board == self.solution

	def valid(self, r, c):
		row, col = self.space
		row += r
		col += c

		if row in range(self.size) and col in range(self.size):
			return True

		return False

	#Prints the current layout of the board
	def getBoard(self):	
		st = ''
		for i in range(self.size):
			for j in range(self.size):
				st +='%2d'%self.board[i,j] + ' '
			st += ('\n')

		print (st)

	def setBoard(self,b):
		self.board = b


	#Overloaded function. Allows printing of objects of class type Board
	def __str__(self):
		st = ''
		for i in range(self.size):
			for j in range(self.size):
				st +='%2d'%self.board[i,j] + ' '
				# print (st)
			st += ('\n')

		# print ("111"+self.solution)
		return st

if __name__ == "__main__":
	b = Board()
	b.getBoard()
	b.makeMove(77)
	b.getBoard()
