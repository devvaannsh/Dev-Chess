# Import the modules
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import QRectF
from main_interface import Ui_main_window       # self-defined module
from validation import ValidMoves               # self-defined module
import sys


class MainWindow(QMainWindow, Ui_main_window):
    """This is the main class which sets up the UI and leads the program ahead. It inherits from two classes, QMainWindow is the pre-defined class and Ui-main_window is the self-defined class which holds the code for the UI"""

    selected_piece = None  # this static variable will hold the current selected piece
    selected_old_square_address = None # this static variable will hold the square (QPushButton's address) from where the piece is to be removed
    selected_old_square_index = None # this static variable will hold the index of the previous square, to update the position dictionary
    valid_moves = []    # this list will store all the valid moves in this class, which the methods will access to get the list of valid moves from the ValidMoves class, we will maintain this list after every operation

    def __init__(self):
        super().__init__()
        self.setupUi(self)      # call the setupUi method from Ui_main_window class, sets up the basic board
        self.pieces_positions() # this method maintains a dictionary that keeps track of the positions of all the pieces
        self.setup_pieces()     # this method is for setting up the pieces initially on the board
        self.squares_signals_slots() # this method just links every square with the method and passes the index of the square to the method 

        self.validate = ValidMoves() # create an instance of the ValidMoves class 


    def squares_signals_slots(self):
        """This method is just for linking every square with a method which will be called whenever a square will be clicked"""

        # make a list of all the squares (these are actually the QPushButtons)
        squares = [self.a1, self.b1, self.c1, self.d1, self.e1, self.f1, self.g1, self.h1, self.a2, self.b2, self.c2, self.d2, self.e2, self.f2, self.g2, self.h2, self.a3, self.b3, self.c3, self.d3, self.e3, self.f3, self.g3, self.h3, self.a4, self.b4, self.c4, self.d4, self.e4, self.f4, self.g4, self.h4, self.a5, self.b5, self.c5, self.d5, self.e5, self.f5, self.g5, self.h5, self.a6, self.b6, self.c6, self.d6, self.e6, self.f6, self.g6, self.h6, self.a7, self.b7, self.c7, self.d7, self.e7, self.f7, self.g7, self.h7, self.a8, self.b8, self.c8, self.d8, self.e8, self.f8, self.g8, self.h8]

        # make a list of all the square_indexes like 'a1', 'a2', ....'h2's
        square_indexes = [f"{row}{col}" for col in range(1, 9) for row in 'abcdefgh']

        # linking all the squares with a method, and passing the square index as an argument to it
        for index, square in enumerate(squares):
            square_index = square_indexes[index]
            square.clicked.connect(lambda _, square_index=square_index: self.square_clicked(square_index))

  
    def pieces_positions(self):
        """This method keeps track of the positions of all the pieces, using a dictionary"""
        
        self.position = {
            'a1' : 'wR',
            'b1' : 'wN',
            'c1' : 'wB',
            'd1' : 'wQ',
            'e1' : 'wK',
            'f1' : 'wB',
            'g1' : 'wN',
            'h1' : 'wR',

            'a2' : 'wP',
            'b2' : 'wP',
            'c2' : 'wP',
            'd2' : 'wP',
            'e2' : 'wP',
            'f2' : 'wP',
            'g2' : 'wP',
            'h2' : 'wP',

            'a7' : 'bP',
            'b7' : 'bP',
            'c7' : 'bP',
            'd7' : 'bP',
            'e7' : 'bP',
            'f7' : 'bP',
            'g7' : 'bP',
            'h7' : 'bP',

            'a8' : 'bR',
            'b8' : 'bN',
            'c8' : 'bB',
            'd8' : 'bQ',
            'e8' : 'bK',
            'f8' : 'bB',
            'g8' : 'bN',
            'h8' : 'bR',
        }


    def setup_pieces(self):
        """
        This method sets up the pieces on the board initially.

        # The first character states whether the first character is white or black.
        # The second character describes the piece.
        """

        # make a list of all the pieces that is to be arranged on the board, along with the squares
        pieces = list(self.position.values())   # fetch all the pieces from the position dictionary
        squares = [self.a1, self.b1, self.c1, self.d1, self.e1, self.f1, self.g1, self.h1, self.a2, self.b2, self.c2, self.d2, self.e2, self.f2, self.g2, self.h2, self.a7, self.b7, self.c7, self.d7, self.e7, self.f7, self.g7, self.h7, self.a8, self.b8, self.c8, self.d8, self.e8, self.f8, self.g8, self.h8]

        # setting the pieces on the related squares
        for index, piece in enumerate(pieces):
            path = f"assets\\pieces_images\\{piece}.svg"
            image = QSvgWidget(path)
            image.setGeometry(0, 0, 90, 85)
            image.setParent(squares[index])
            image.show()


    def square_clicked(self, square_index):
        """This method will get triggered when any square will get clicked"""

        # for selecting a piece
        if square_index in self.position.keys() and self.position[square_index][0] == 'w' and MainWindow.selected_piece is None:  # to make sure that user selects a white piece, and no other piece is selected at the time
            self.select_piece(square_index)
        elif square_index in self.position.keys() and self.position[square_index][0] == 'w' and MainWindow.selected_piece is not None: # when a piece is already selected and user wants to change the selected piece
            self.change_selected_piece(square_index)
        else:   # means user either clicked on a square with a black piece or no piece at all, so we move the selected piece
            if MainWindow.selected_piece is not None:   # only call the move_piece method when some piece is selected by the user
                self.move_piece(square_index, self.sender())    # here self.sender() and square_index is for the square where the piece must be moved


    def select_piece(self, square_index):
        """This method is for selecting the piece initially (from initially it means that no piece is selected right then)"""

        # setting the values of the static variable to the current selected piece
        MainWindow.selected_piece = self.position[square_index] # to select the piece
        MainWindow.selected_old_square_address = self.sender()  # to keep track of the square from where the piece is to be removed
        MainWindow.selected_old_square_index = square_index  # to keep track of the square index to update the position dictionary

        self.selected_square_background(MainWindow.selected_old_square_address)   # this method will change the background-color of the selected square

        # fetching all the valid moves for the piece (MainWindow.valid_moves stores the index of all the valid squares)
        MainWindow.valid_moves = self.validate.menu(MainWindow.selected_piece, MainWindow.selected_old_square_index, self.position)
        self.valid_moves_square_background(MainWindow.valid_moves)  # for changing the background color of all the square which are valid


    def valid_moves_square_background(self, valid_moves):
        """This method is responsible to add an image that helps identify the valid squares for the user"""
        for valid_move_index in valid_moves:

            if valid_move_index in self.position.keys():    # means that some black is present on the square, so here we don't add the image but instead change the background color of the square
                valid_move_square_address = self.findChild(QPushButton, valid_move_index)   # getting the address of the square from the index of it
                if valid_move_square_address is not None:   # make sure that the address is found
                    if (ord(valid_move_index[0]) + int(valid_move_index[1])) % 2 == 0:  # this is black
                        valid_move_square_address.setStyleSheet("background-color : #646e40;""border: 0px solid black;")
                    else:   # this is white
                        valid_move_square_address.setStyleSheet("background-color : #82976a;""border: 0px solid black;")


            else:   # means no piece is present on the square
                valid_move_square_address = self.findChild(QPushButton, valid_move_index)   # getting the address of the square from the index of it
                if valid_move_square_address is not None:   # make sure that the address is found

                    # find out if the square is black or white [logic is that if the ascii value of the file + the rank becomes a odd number then the square is black, else white]
                    if (ord(valid_move_index[0]) + int(valid_move_index[1])) % 2 == 0:  # this is black
                        path = f"assets\\valid_moves_images\\valid_move_black_image.svg"
                        image = QSvgWidget(path)
                        image.setGeometry(0, 0, 90, 85)
                        image.setParent(valid_move_square_address)
                        image.show()

                    else:   # this is white
                        path = f"assets\\valid_moves_images\\valid_move_white_image.svg"
                        image = QSvgWidget(path)
                        image.setGeometry(0, 0, 90, 85)
                        image.setParent(valid_move_square_address)
                        image.show()

    
    def reset_valid_moves_square_background(self, valid_moves):
        """This method is responsible to reset the valid squares to its normal state [remove the images]"""
        for valid_move_index in valid_moves:
            if valid_move_index in self.position.keys():    # means that some black is present on the square, so we reset the background color
                valid_move_square_address = self.findChild(QPushButton, valid_move_index)   # getting the address of the square from the index of it
                if valid_move_square_address is not None:   # make sure that the address is found
                    background_color = valid_move_square_address.palette().color(QPalette.Background)
                    if background_color.name() == "#646e40":    # for black
                        valid_move_square_address.setStyleSheet("background-color : #b58863;""border: 0px solid black;")
                    if background_color.name() == "#82976a":    # for white
                        valid_move_square_address.setStyleSheet("background-color : #f0d9b5;""border: 0px solid black;")
        
            else:   # means no piece is on the square, so we remove the image
                valid_move_square_address = self.findChild(QPushButton, valid_move_index)   # getting the address of the square from the index of it
                if valid_move_square_address is not None:   # make sure that the address is found
                    remove_image = valid_move_square_address.findChildren(QSvgWidget)[0]
                    remove_image.setParent(None)


    def selected_square_background(self, square):
        """This method is responsible to change the background color of the selected square"""
        background_color = square.palette().color(QPalette.Background)   # get the background color of the square
        if background_color.name() == "#b58863":    # for black
            square.setStyleSheet("background-color : #656f41;""border: 0px solid black;")
        if background_color.name() == "#f0d9b5":    # for white
            square.setStyleSheet("background-color : #829769;""border: 0px solid black;")


    def reset_selected_square_background(self, square):
        """This method will get triggered when user changes their selection. It resets the background-color of the previously selected square"""
        background_color = square.palette().color(QPalette.Background)   # get the background color of the square
        if background_color.name() == "#656f41":    # for black
            square.setStyleSheet("background-color : #b58863;""border: 0px solid black;")
        if background_color.name() == "#829769":    # for white
            square.setStyleSheet("background-color : #f0d9b5;""border: 0px solid black;")


    def change_selected_piece(self, square_index):
        """This method will get triggered when user wants to change their selection, i.e. when they selected a different piece and then changed the selection to another piece"""

        # reset the backgorund color of the previously selected square to normal
        self.reset_selected_square_background(MainWindow.selected_old_square_address)
        # reset the valid squares for the previous state to normal
        self.reset_valid_moves_square_background(MainWindow.valid_moves)

        MainWindow.valid_moves = [] # reset back the valid moves list to empty
        # now just call select_piece method to select the new piece
        self.select_piece(square_index)


    def move_piece(self, square_index, square_index_address):
        """This method is responsible to move the selected piece from its initial square to the new square"""
        # make move only if the index is in the list of valid moves
        if square_index in MainWindow.valid_moves:
            if square_index in self.position.keys(): # checks if there is any black piece on the square
                remove_piece = square_index_address.findChildren(QSvgWidget)[0]    # for removing the black piece from the board
                remove_piece.setParent(None)

            # reset the background color of the square from where the square was moved
            self.reset_selected_square_background(MainWindow.selected_old_square_address)
            # reset the valid moves images from the valid squares to its normal state
            self.reset_valid_moves_square_background(MainWindow.valid_moves)

            # add the selected piece to the new square
            piece = MainWindow.selected_old_square_address.findChildren(QSvgWidget)[0]    # find out which piece is inside the square from where we are removing the piece
            piece.setParent(square_index_address)  # change the parent to the new square which is clicked
            piece.show()    # display the image

            # replace the old_square_index with the new_square_index to keep the position dictionary updated
            del self.position[MainWindow.selected_old_square_index]
            self.position[square_index] = MainWindow.selected_piece

            # set the static variables to None as we have done the operation
            MainWindow.selected_piece = None   
            MainWindow.selected_old_square_address = None
            MainWindow.selected_old_square_index = None
            MainWindow.valid_moves = []



# Initialize the application, display the main window and start the application event loop
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    application.exec_()