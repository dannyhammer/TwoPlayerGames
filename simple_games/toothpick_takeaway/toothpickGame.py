###
# TOOTHPICK TAKEAWAY
###
###
#game skeleton

#take_sticks(player)
#start with N sticks, ask player how many to take
#update num sticks, check for winner

#game_two_human():
# Creates 2 players(human)then uses functions to play the game normally

#Game_one_human():
# asks if the human would like to be player 1 or 2
# Then plays the game normally

#Game_no_human(strat, player = 1):
# creates two Computer players
# strat(int) = (0,1,2)the number of computer players using the found strategy
# player(int) = (1,2) the player to recieve the strat if only one will recieve it

###
# CODE
import Player as P
#the default number of sticks to play the game with
DEFAULT = 10

def run_games(int):
    for x in int:
        play_game(3)
def play_game(type, strat = 0):
    """
    type(int): a 1,2,3 for what type of game to play
    strat
    """
    game_two_human()
    game_one_human()
    game_no_human(strat, player)

def swap_turn(p1, p2):
    p1.change_turn()
    p2.change_turn()


def game_two_human(p1,p2):
    """
    This function will run a game with only both human player

    Args:
    p1: player one, a human
    p2: player two, a human

    Return:
    A string depending on which player won
    """
    num_sticks = DEFAULT
    while(num_sticks > 0):
        if(p1.get_turn()):
            num_sticks -= p1.human_move(num_sticks)
            if(num_sticks == 0 ):
                return("Player 1 Wins, Thank you for playing")
            p1.changeturn()
            p2.changeturn()
        else:
            num_sticks -= p2.human_move(num_sticks)
            if(num_sticks == 0 ):
                return("Player 2 Wins, Thank you for playing")
            p2.changeturn()
            p1.changeturn()





def game_one_human(p1,p2,strat):
    """
    This function will run a game with only one human player

    Args:
    p1: player one, can be human or computer
    p2: player two, can be human or computer
    strat: whether or not the cpu plays with a strategy

    Return:
    A string depending on which player won
    """
    num_stick = DEFAULT
    while(num_sticks > 0):
        #human player 1
        if(p1.get_type == "h"):
            #human player 1 turn
            if(p1.get_turn()):
                num_sticks -= p1.human_move(num_sticks)
                if(num_sticks == 0 ):
                    return("Player 1 Wins, Thank you for playing")
                p1.changeturn()
                p2.changeturn()
            #cpu player 2 turn
            else:
                #no strat
                if(strat == False):
                        num_sticks -= p2.human_move(num_sticks)
                        if(num_sticks == 0 ):
                            return("Player 2 Wins, Thank you for playing")
                        p2.changeturn()
                        p1.changeturn()
                #with strat
                else:

                        num_sticks -= p2.human_move(num_sticks)
                        if(num_sticks == 0 ):
                            return("Player 2 Wins, Thank you for playing")
                        p2.changeturn()
                        p1.changeturn()
        #cpu player 1
        else:
            #no strat
            if(strat == False):
                if(p1.get_turn()):
                    num_sticks -= p1.comp_move_rand(num_sticks)
                    if(num_sticks == 0 ):
                        return("Player 1 Wins, Thank you for playing")
                    p1.changeturn()
                    p2.changeturn()
                else:
                    num_sticks -= p2.human_move(num_sticks)
                    if(num_sticks == 0 ):
                        return("Player 2 Wins, Thank you for playing")
                    p2.changeturn()
                    p1.changeturn()
            #with strat
            else:
                if(p1.get_turn()):
                    num_sticks -= p1.comp_move_strat(num_sticks)
                    if(num_sticks == 0 ):
                        return("Player 1 Wins, Thank you for playing")
                    p1.changeturn()
                    p2.changeturn()
                else:
                    num_sticks -= p2.human_move(num_sticks)
                    if(num_sticks == 0 ):
                        return("Player 2 Wins, Thank you for playing")
                    p2.changeturn()
                    p1.changeturn()




#def game_no_human():
