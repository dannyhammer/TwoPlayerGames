###
# player class

#FIELDS
# turn(boolean): tells whos turn it is

#comp_move_rand(num_sticks)
# This function will make a random legal move, either 1 or 2,

#comp_move_strat(num_sticks)
# this function will take the number of sticks in, and use our found strategy
#   to make the best move possible

#human_move()
# This function will simply take human input to make a legal move

#getter/setter
# get turn
# set turn

###
import random as r

class Player:

    turn = False
    type = "0"
    #I dont believe I need to initialize any fields for the class
    def __init__(type = "c"):
        self.type = type

    #GET SET CHANGE
    def get_type():
        return self.type

    def set_type(type):
        self.type = type

    def get_turn():
        return self.turn

    def set_turn(set):
        if(type(set) != bool):
            self.turn = set
        else:
            print("Invalid turn type, must be boolean")

    def change_turn():
        self.turn = not self.turn

    #OTHER STUFF
    def human_move(num_left):
        """
        This fucntion makes a human players move

        Args:
        num_left: the number of sticks left in the pile
        """
        if(num_left >= 2):
            to_take = int(input("1 or 2 sticks?"))
            if(not 0 < to_take < 3):
                while(not 0 < to_take < 3):
                    print("Invalid selection, try again")
                    to_take = int(input("1 or 2 sticks?"))
        else:
            to_take = int(input("Enter 1 to take the last stick"))
            if(not 0 < to_take < 2):
                while(not 0 < to_take < 32):
                    print("Invalid selection, try again")
                    to_take = int(input("Enter 1 to take the last stick"))
        return to_take

    def comp_move_rand(num_left):
        """
        This Function makes a move based on rng

        Args:
        num_left: the number of sticks left in the pile
        """
        if(num_left >= 2):
            to_take = r.randrange(0,2)
        else:
            to_take = 1
        return to_take

    def comp_move_strat(num_left):
        """
        This function will take the number of sticks remaining and make the best
        move based on out found strategy

        Args:
        num_left: the number of sticks left in the pile
        """
        if(num_left % 3 == 0):
            to_take = 1
        elif(num_left % 3 == 1):
            to_take = 1
        else:#num_left % 3 == 2
            to_take = 2
        return to_take

