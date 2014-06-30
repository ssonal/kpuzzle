

from __future__ import print_function

import os
import os.path
import copy
import timeit

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
		if self.clear_screen:
				os.system(Game.__clear)
		else:
			print('\n')

		print(self)
		m = {72:"UP ",80:"DOWN ",77:"RIGHT ",75:"LEFT "}
		start = timeit.default_timer()
		moves = self.astar(copy.deepcopy(self.board))
		stop = timeit.default_timer()
		m1 = ''.join([m[x] for x in moves])
		
		print ("Game solved!\nTime taken:%fs\nMoves to solution: %2d" %(stop-start,len(moves)))
		print ("Solution:"+m1)


		for move in moves:
			self.board.makeMove(move)

			self.score += 1
			print(self)
			raw_input('Press any key to continue')

		print ('You won!')

	def astar(self,puzzle,heuristic=True):
		counter = 0
		try:
			queue = PriorityQueue()
			priority = 0
			currentmoves = []
			parentBoard = None
			while True:
				# print(puzzle)
				if puzzle.won():
					print ("Number of nodes expanded: %d"%counter)
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
						if heuristic:
							p += manhattanDistance(p1)+hammingDistance(p1)#linearConflict(p1)
						queue.push((p1,c),p)

					counter += 1
					parentBoard = copy.deepcopy(puzzle.board)
					b,m = queue.pop()
					puzzle = b
					currentmoves = m

					# priority = p

					# raw_input(' ')

		except KeyboardInterrupt:
			print(counter)

	def __str__(self):
		s1 = '\n\n\n'+str(self.board)+'\nScore:'+str(self.score)+'\n'
		return s1

if __name__=='__main__':

	g = Game(mode='ai')
	g.gameLoop()
	# print(linearConflict(g.board))
# 12783 7450