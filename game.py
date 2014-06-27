

from __future__ import print_function

import os
import os.path

from layout import Board
import keypress

class Game(object):

	__clear = 'cls' if os.name == 'nt' else 'clear'

	def __init__(self, mode='user',size=4, clear_screen=True,**kws):
		self.board = Board(size, **kws)
		self.score = 0
		self.clear_screen = clear_screen
		self.mode = mode


	def readMove(self):
		key = keypress.getKey()
		return key

	def gameLoop(self):
		if self.mode == 'user':
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


	def ai(self):
		pass

	def __str__(self):
		s1 = '\n\n\n'+str(self.board)+'\nScore:'+str(self.score)+'\n'
		return s1

if __name__=='__main__':
	g = Game()
	print (g)