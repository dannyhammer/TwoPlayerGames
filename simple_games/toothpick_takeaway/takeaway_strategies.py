from random import choice

def random_move(board):
    move_selected = False
    possible_moves = [1,2]
    moves_tried = []
    while not(move_selected):
        move_to_try = choice(possible_moves)
        if (board.state - move_to_try) < 0:
            moves_tried.append(move_to_try)
        else:
            move_selected = True
        if set(moves_tried) == set(possible_moves):
            return None
         
        return move_to_try
      
def always_take_one(board):
    if (int(board.state) - 1) < 0: #check for legality
        return None
    else:
        return 1
       
def always_take_two(board):
    if (int(board.state) - 2) < 0: #check for legality
        return None
    else:
        return 2
       
def human_player(board):
    return int(input("Please make your move: \n"))
    
 
