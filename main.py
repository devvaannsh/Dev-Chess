# Import the modules
from PyQt5.QtWidgets import QApplication, QMainWindow  
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtGui import QPalette
from main_interface import Ui_main_window       # self-defined module
import sys


class MainWindow(QMainWindow, Ui_main_window):
    """This is the main class which sets up the UI and leads the program ahead. It inherits from two classes, QMainWindow is the pre-defined class and Ui-main_window is the self-defined class which holds the code for the UI"""

    selected_piece = None  # this static variable will hold the current selected piece
    previous_square = None # this static variable will hold the square from where the piece is to be removed
    previous_square_index = None # this static variable will hold the index of the previous square, to update the position dictionary

    def __init__(self):
        super().__init__()
        self.setupUi(self)      # call the setupUi method from Ui_main_window class, sets up the basic board
        self.pieces_positions() # this method maintains a dictionary that keeps track of the positions of all the pieces
        self.setup_pieces()     # this method is for setting up the pieces initially on the board
        self.squares_signals_slots() # this method just links every square with the method and passes the index of the square to the method 


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
        """
        This method gets triggered when any square gets clicked. 
        If user clicks on a piece to select it, the piece, square gets selected and the background color of the selected square changes, to let user know that the square is selected
        If user clicks on a piece to move it, the piece moves to the new square from the old one.
        """
        
        # this code will get executed when user clicks on a square with white piece. It basically selects the piece
        if square_index in self.position.keys() and self.position[square_index][0] == 'w':
            # to change the background color of the square selected
            background_color = self.sender().palette().color(QPalette.Background)   # get the background color of the square
            if background_color.name() == "#b58863":    # for black
                self.sender().setStyleSheet("background-color : #a57742;""border: 0px solid black;")
            if background_color.name() == "#f0d9b5":    # for white
                self.sender().setStyleSheet("background-color : #d4c3a0;""border: 0px solid black;")
                
            # reset the background-color of the first square if two white pieces are selected one after another(means that user selects a piece and then changes the selection to another piece)
            if MainWindow.previous_square is not None and self.sender() != MainWindow.previous_square:
                background_color = MainWindow.previous_square.palette().color(QPalette.Background)
                if background_color.name() == "#a57742":    # for black
                    MainWindow.previous_square.setStyleSheet("background-color : #b58863;""border: 0px solid black;")
                if background_color.name() == "#d4c3a0":    # for white
                    MainWindow.previous_square.setStyleSheet("background-color : #f0d9b5;""border: 0px solid black;")

            MainWindow.selected_piece = self.position[square_index] # to select the piece
            MainWindow.previous_square = self.sender()  # to keep track of the square from where the piece is to be removed
            MainWindow.previous_square_index = square_index  # to keep track of the square index to update the position dictionary
         
        # this code will get executed when user clicks on a square with no piece or a black piece on it
        else:
            if self.selected_piece is not None:     # make sure that some piece is selected or else we don't have to do anything
                
                # to remove the previous piece from the square (for example when taking a black piece, we remove the black piece first)
                if len(self.sender().findChildren(QSvgWidget)) > 0: # check if there is some piece on the square previously, if yes remove the piece 
                    remove_piece = self.sender().findChildren(QSvgWidget)[0]
                    remove_piece.setParent(None)

                piece = MainWindow.previous_square.findChildren(QSvgWidget)[0]    # find out which piece is inside the button, we use [0] because findChildren method returns a list of all the children, in our case there is only one children so we use [0]
                piece.setParent(self.sender())  # change the parent to the new square which is clicked
                piece.show()    # display the image

                # replace the old_square_index with the new_square_index to keep the position dictionary updated
                if MainWindow.previous_square_index in self.position.keys():
                    del self.position[MainWindow.previous_square_index]
                    self.position[square_index] = MainWindow.selected_piece

                # reset the background color of the square which was selected to normal
                background_color = MainWindow.previous_square.palette().color(QPalette.Background)
                if background_color.name() == "#a57742":    # for black
                    MainWindow.previous_square.setStyleSheet("background-color : #b58863;""border: 0px solid black;")
                if background_color.name() == "#d4c3a0":    # for white
                   MainWindow.previous_square.setStyleSheet("background-color : #f0d9b5;""border: 0px solid black;")

                # set the static variables to None as we have done the operation
                MainWindow.selected_piece = None   
                MainWindow.previous_square = None
                MainWindow.previous_square_index = None


# Initialize the application, display the main window and start the application event loop
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    application.exec_()