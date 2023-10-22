import random
from validation import ValidMoves   # self defined module

class ComputerMove():
    """This is the main class which will generate the move, that is to be played by the computer"""

    def __init__(self):
        self.validate = ValidMoves() # creating an instance of ValidMoves class


    def move(self, position):
        """This is the method which will be called by main.py. This will return a list[3] where 0th item will be the index of the square where the piece is to be moved, 1st item will be the index of the square from where the piece is to be moved and 2nd item will be the piece that is to be moved"""
        self.movement = []  # this list will store the movement that is to be made [to, from, piece]       
        self.position = position # this is the main dictionary which we maintain to keep track of the pieces and in which square they are in
        self.generate_move()  # calling the method which will generate a random move
        return self.movement   # return the movement list 
    
    def generate_move(self):
        """This method will generate a random move, get the movement list ready which will be returned by the move method"""
        self.active_black_pieces = []   # this list will have dictionaries inside it, which will store all the black pieces and their index  format -> [{'a1' : 'bN'}, {'b7;'bP'}]
        for key, value in self.position.items():    # here key is the index and value is the piece
            if value[0] == 'b': # check if the piece is a black piece
                temp = {}       # create a temporary dictionary to append it to the main list
                temp[key] = value
                self.active_black_pieces.append(temp)

        while len(self.active_black_pieces) != 0:   # this will actually work as an infinite loop, because we will always have the king present on the board but still for development cases, we make sure that there is some piece on the board
            # picking up a random number and getting the piece from the active_black_pieces list 
            random_number = random.randint(0, len(self.active_black_pieces)-1)   
            random_piece = self.active_black_pieces[random_number]      # random piece is now a dictionary

            from_index = next(iter(random_piece))    # gets the index of the piece [this is the index from where the piece is to be moved]
            piece = random_piece[from_index]         # gets the actual piece

            valid_moves = self.validate.menu(piece, from_index, self.position)   # calls the manu method of the ValidMoves class by using the object, this returns a list of all the valid moves for that piece .... store the list in valid_moves
            if len(valid_moves) > 0:    # check is the piece can be moved, if there is atleast one valid move for the piece
                random_number = random.randint(0, len(valid_moves)-1) # out of all the valid moves for the piece, pick one out randomly
                to_index = valid_moves[random_number]     # this is the piece where the piece is to be moved
                self.movement = [to_index, from_index, piece]   # updating the list
                break

            else:   # if no valid moves are present for the piece, remove the piece from the list of active_black_pieces
                self.active_black_pieces.pop(random_number)








