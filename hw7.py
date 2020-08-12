#Purpose: Takes in an integer input and plugs it into the collatz conjecture.
#Input Parameter(s): A positive integer input.
#Return Value(s): Returns the collatz sequence from n to 1 inclusive.
def collatz(n):
    list1 = [n]
    if n == 1:
        return [n]  
    elif n%2 == 0:
        list1.extend(collatz(n//2))
    else:
        list1.extend(collatz(n*3+1))
    return list1

#Purpose: Takes in a list of integers and returns the minimum value within the
#         list.
#Input Parameter(s): Takes in a list of integers.
#Return Value(s): Returns the minimum value from the inputted list of integers.
def find_min(num_list):
    if len(num_list) == 1:
        return num_list[0]
    min_num = num_list[0]
    if min_num < find_min(num_list[1:]):
        return min_num
    else:
        return find_min(num_list[1:])

#Purpose:
#Input Parameter(s):
#Return Value(s):

def play_games(n):
    winnars = []
    for i in range(n):
        game = tic_tac_toe()
        winnars.append(game)
    print("X wins:",winnars.count('X'))
    print("O wins:",winnars.count('O'))
    print("Draw:",winnars.count('D'))
    
#Purpose:
#Input Parameter(s):
#Return Value(s):
    
def tic_tac_toe():
    board = ['-']*9
    turn = 'X'
    while winner(board) == '-':
        slots = open_slots(board)
        pick = random.choice(slots)
        if turn == 'X':
            board[pick] = 'X'
            turn = 'O'
        elif turn == 'O':
            scores = []
            for i in slots:
                copyboard = board[:]
                copyboard[i] = 'O'
                result = force_win(copyboard)
                scores.append(result)
            best_score = find_min(scores)
            s_idx = slots[scores.index(best_score)]
            board[s_idx] = 'O'
            turn = 'X'
    return winner(board)

#Purpose:
#Input Parameter(s)
#Return Value(s):

def display_board(board):
    for i in range(3):
        print(' '.join(board[3*i:3*i+3]))
    print()
    
#Purpose
#Input Parameter(s)
#Return Value(s):

def winner(board):
    wins = [[0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]
    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] == 'X':
            return 'X'
        if board[win[0]] == board[win[1]] == board[win[2]] == 'O':
            return 'O'
    if '-' in board:
        return '-'
    return 'D'

#Purpose:
#Input Parameter(s):
#Return Value(s):

def open_slots(board):
    ret = []
    for i in range(len(board)):
        if board[i] == '-':
            ret.append(i)
    return ret

#Purpose:
#Input parameter(s):
#Return Value(s):
def find_max(num_list):
    if len(num_list) == 1:
        return num_list[0]
    max_num = num_list[0]
    if max_num > find_min(num_list[1:]):
        return max_num
    else:
        return find_max(num_list[1:])
#Purpose:
#Input Parameter(s):
#Return Value(s):
import random
board = ['X', 'O', 'X', 'X', 'O', 'X', '-', '-', 'O']
def force_win(board):
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    elif winner(board) != '-':
        return 0
    slots = open_slots(board)
    x = len(slots)
    scores = []
    best_score = None
    if x % 2 == 1:
        for i in slots:
            copyboard = board[:]
            copyboard[i] = 'X'
            result = force_win(copyboard)
            scores.append(result)
        best_score = find_max(scores)
    else:
        for i in slots:
            copyboard = board[:]
            copyboard[i] = 'O'
            result = force_win(copyboard)
            scores.append(result)
        best_score = find_min(scores)
    s_idx = slots[scores.index(best_score)]
    if x % 2 == 1:
        board[s_idx] = 'X'
    else:
        board[s_idx] = 'O'
    return best_score
    
            
    

        
    
