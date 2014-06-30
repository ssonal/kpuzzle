

from __future__ import print_function
import argparse
import sys
from game import Game



def parsed_args():
	parser = argparse.ArgumentParser(description='Kpuzzle in your terminal')

	parser.add_argument('--size', dest='size', type=int,
                        default=4, help='size of board')

	parser.add_argument('--mode', dest='mode', type=str,
						default='ai', help='user/AI')

	parser.add_argument('--shuffle', dest='count',type=int,
						default=80,help='Indicate degree of difficulty of board')

	return vars(parser.parse_args())


def start_game():

	args = parsed_args()

	Game(**args).gameLoop()


if __name__=="__main__":
	start_game()


