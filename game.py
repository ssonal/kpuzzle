

from __future__ import print_function

import os
import os.path
import copy
from layout import Board
from util import *
import keypress


class Game(object):

	__clear = 'cls' if os.name == 'nt' else 'clear'

	def __init__(self,count=85, mode='user',size=4, clear_screen=True,**kws):
		self.board = Board(size,count, **kws)
		self.score = 0
		self.clear_screen = clear_screen
		self.mode = mode

	def getBoard(self):
		return self.board

	def readMove(self):
		key = keypress.getKey()
		return key

	def gameLoop(self):
		if self.mode == 'ai':
			print ('ai')
			self.ai()
			return 0
		else:
			try:
				while(True):
					if self.clear_screen:
						os.system(Game.__clear)
					else:
						print('\n')

					print(self)

					if self.board.won():
						break
					m = self.readMove()
					# print(m)
					if self.board.makeMove(m):
						self.score += 1

			except TypeError:
				return 0

	        print('You won!' if self.board.won() else 'Game Over')
	        return self.score

	def ai(self):
		try:
		
			if self.clear_screen:
					os.system(Game.__clear)
			else:
				print('\n')

			print(self)
			moves = self.astar(copy.deepcopy(self.board))
			print (moves)
			print (len(moves))

			for move in moves:
				self.board.makeMove(move)

				self.score += 1
				print(self)
				raw_input(' ')
		except TypeError:
			return 0

		print ('You won!')

	def astar(self,puzzle):
		queue = PriorityQueue()
		priority = 0
		currentmoves = []
		counter = 0
		parentBoard = None
		while True:
			# print(puzzle)
			if puzzle.won():
				print (counter)
				return currentmoves
			else:
				# print (priority)
				moves = puzzle.getMoves()

				for move in moves:
					p1 = copy.deepcopy(puzzle)
					c = copy.deepcopy(currentmoves)
					p1.makeMove(move)
					if p1.board == parentBoard:
						continue
					c.append(move)
					p = len(currentmoves)
					p += manhattanDistance(p1)+hammingDistance(p1)#linearConflict(p1)
					queue.push((p1,c,p),p)

				counter += 1
				parentBoard = copy.deepcopy(puzzle.board)
				b,m,p = queue.pop()
				puzzle = b
				currentmoves = m

				priority = p

				# raw_input(' ')

	def __str__(self):
		s1 = '\n\n\n'+str(self.board)+'\nScore:'+str(self.score)+'\n'
		return s1

if __name__=='__main__':

	g = Game(mode='ai')
	g.gameLoop()
	# print(linearConflict(g.board))
# 12783 7450