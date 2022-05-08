from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Игрок 1: Кем Вы хотите играть, X или O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#player_input()

def place_marker(board, marker, position):
    board[position] = marker

# place_marker(test_board,'$',8)
# display_board(test_board)

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # горизонталь сверху
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # горизонталь в середине
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # горизонталь снизу
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # вертикаль слева
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # вертикаль в середине
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # вертикаль справа
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # диагональ
            (board[9] == mark and board[5] == mark and board[1] == mark))  # диагональ


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Игрок 2'
    else:
        return 'Игрок 1'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Выберите следующую клетку: (1-9) '))

    return position


def replay():
    return input('Вы хотите сыграть снова? Yes или No: ').lower().startswith('y')