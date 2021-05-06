# ATBS - Chapter 5
# tic-tac-toe


board = {'tl': ' ', 'tm':' ', 'tr':' ',
         'ml':' ','mm':' ','mr':' ',
         'bl':' ','bm':' ','br':' '}

def printBoard(board):
    print(board['tl'] + '|' + board['tm'] + '|' + board['tr'])
    print('-+-+-')
    print(board['ml'] + '|' + board['mm'] + '|' + board['mr'])
    print('-+-+-')
    print(board['bl'] + '|' + board['bm'] + '|' + board['br'])

printBoard(board)
turn = 'x'

for i in range(9):
    print('turn for ' + turn)
    print('enter your move...')
    move = input()

    board[move] = turn
    printBoard(board)
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'

