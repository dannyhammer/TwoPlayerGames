class Game:
"""
This implements a Game that takes a list/set of players, a referee, and a board.
It automates the process of playing the game, and returns a winner.

TODO: Finish Docstring for methods and other attributes. 
"""

#TODO: initialize
#should take as input a board, a player_list, a referee, and a first player
#if no first player given, make it be the first player in the list. 

def play(): 
"""
TODO: Docstring
"""
   game_over = False 
   while(not(game_over)):
      player_move = current_player.move(board.state) #select a player move based on state of board
      if referee.is_legal(player_move, board.state):  #check to see if move is legal
         next_player, new_state = board.update(current_player, player_move, board.state) #update board if legal
         if referee.is_winning(board.state): #check to see if move has won
            winning_player = current_player #set winning_player and return if needed
            return winning_player
         else: #if no one won, update current player and board
            board.state = new_state
            current_player = next_player
            
         
            
            
         
         
      
