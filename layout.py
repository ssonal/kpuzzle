from __future__ import print_function
from random import randint
from copy import deepcopy
import keypress

class Board(object):


	#map for directions of movement
	__dirs = {
        keypress.UP:      (1,0),
        keypress.DOWN:    (-1,0),
        keypress.LEFT:    (0,1),
        keypress.RIGHT:   (0,-1),
    }

      #   1
      # 3   4
      #   2

	def __init__(self,size=4,other=None,**kws):
		self.size = size
		self.board, self.space, self.solution = self.getNewBoard()
		if other:
			self.dict = deepcopy(other.__dict__)


	#Initialization funtion. Creates a new k-puzzle board randomly
	def getNewBoard(self):
		nums = range((self.size**2))
		# print (nums)


		board, space = self.shuffle(deepcopy(nums))

		b = {}
		k=0
		for i in range(self.size):
			for j in range(self.size):
				b[i,j] = nums[k]
				k+=1
		return board, space, b

	def shuffle(self, nums):
		for i in range(self.size**2):
			r = randint(i,(self.size**2)-1)
			temp = nums[i]
			nums[i] = nums[r]
			nums[r] = temp
		# print (nums)
		b = {}
		k=0
		space = None
		for i in range(self.size):
			for j in range(self.size):
				b[i,j]=nums[k]
				if nums[k]==0:
					space = (i,j)
				k += 1

		return b,space
	
	def makeMove(self,dire):
		direction = self.__dirs.get(dire)
		# print (self.space)
		# print (direction)
		if self.valid(*direction):
			direction = (self.space[0]+direction[0],self.space[1]+direction[1])
			# print (direction) 
			self.board[self.space] = self.board[direction]
			self.board[direction] = 0
			self.space = direction
			return True

		return False

	def won(self):
		# print (self.board)
		# print (self.solution)
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
		# for i in range(self.size):
		# 	for j in range(self.size):
		# 		print(self.board[i,j],end=' ')
		# 		# pass
		# 	print(end='\n')

		# print(self.board)
		# print(self.solution)	
		st = ''
		for i in range(self.size):
			for j in range(self.size):
				st +='%2d'%self.board[i,j] + ' '
				# print (st)
			st += ('\n')

		print (st)


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
	b.makeMove(119)
	b.getBoard()
	# print 'hello'
	# print (b)