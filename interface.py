

from __future__ import print_function
import argparse
import sys
from game import Game



def parsed_args():
	parser = argparse.ArgumentParser(description='Kpuzzle in your terminal')

	parser.add_argument('--size', dest='size', type=int,
                        default=3, help='size of board')

	parser.add_argument('--mode', dest='mode', type=str,
						default='user', help='user/AI')

	return vars(parser.parse_args())


def start_game():

	args = parsed_args()

	Game(**args).gameLoop()


if __name__=="__main__":
	start_game()


