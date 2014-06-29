

from __future__ import print_function

import os
import os.path
import copy
from layout import Board
from util import *
import keypress


class Game(object):

	__clear = 'cls' if os.name == 'nt' else 'clear'

	def __init__(self, mode='user',size=3, clear_screen=True,**kws):
		self.board = Board(size, **kws)
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
	  #   else:
			# self.ai()
			# return 0


	def ai(self):
		try:
		
			if self.clear_screen:
					os.system(Game.__clear)
			else:
				print('\n')

			print(self)
			queue = PriorityQueue()
			moves = self.bfs(copy.deepcopy(self.board),queue)
			print (moves)
		except TypeError:
			return 0
		# pass


	def bfs(self, puzzle,queue,priority = 0):
		print(puzzle)
		# a = input( ' ')
		# queue = PriorityQueue()
		t = puzzle.won()
		if puzzle.getSoln() == puzzle:
			return ' '
		else:
			moves = puzzle.getMoves()
			print (moves)
			for move in moves:
				queue.push((puzzle.board,move),priority)

			p1 = copy.deepcopy(puzzle)
			b,m = queue.pop()
			# print(b)
			# print(m)
			raw_input(' ')
			p1.board = b
			p1.makeMove(m)
			priority+=1
			return str(move)+' '+self.bfs(p1,queue,priority) 



	def __str__(self):
		s1 = '\n\n\n'+str(self.board)+'\nScore:'+str(self.score)+'\n'
		return s1

if __name__=='__main__':
	g = Game(mode='ai')
	g.gameLoop()
	# print (g)
	# print (manhattanDistance(g.getBoard()))
	# print ('misplaced:%d' %	misplaced(g.getBoard()))