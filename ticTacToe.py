import random
theBoard={'top-L':' ', 'top-M':' ', 'top-R':' ',
'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
'low-L':' ', 'low-M':' ', 'low-R':' '}

initialTurn=['X','O']
firstTurn = random.choice(initialTurn)


def printBoard(board):
	print(board['top-L'] +'|'+board['top-M']+'|'+board['top-R'])
	print('-+-+-')
	print(board['mid-L'] +'|'+board['mid-M']+'|'+board['mid-R'])
	print('-+-+-')
	print(board['low-L'] +'|'+board['low-M']+'|'+board['low-R'])
	
turn = firstTurn
for i in range(9):
	printBoard(theBoard)
	print('Turn for ' + turn + '. Move on which space?')
	move = input()
	theBoard[move] = turn
	#refactor:add exception handlers for move
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'
		#refactor: clear board when game is done and restart
	for i, v in theBoard:
		if 

		#refactor: end game when values arlign


printBoard(theBoard)

