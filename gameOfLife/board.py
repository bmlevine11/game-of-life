from cell import cell
from pprint import pprint

class board():

	# def __init__(self, size):
	# 	#create a game board of user defined size
	size = 3

	board = [[cell(i,j,False) for j in range(size)] for i in range(size)]

	pprint(board)
	pprint(board[1][1])