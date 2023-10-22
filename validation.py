
class ValidMoves():
    """ This class is responsible for making only valid moves so that no invalid moves can be played"""

    def menu(self, piece_to_move, index_of_piece, position):
        """This method takes three parameters, one is the piece, the other is the position of the piece and the third is the dictionary which stores the position of all the pieces"""
        self.piece_to_move = piece_to_move
        self.index_of_piece = index_of_piece
        self.position = position

        self.valid_moves = []   # this list will store all the valid moves for the piece that is selected

        # for white rook 
        if self.piece_to_move == 'wR':
            self.white_rook()

        # for white knight
        elif self.piece_to_move == 'wN':
            self.white_knight()

        # for white bishop
        elif self.piece_to_move == 'wB':
            self.white_bishop()

        # for white queen
        elif self.piece_to_move == 'wQ':
            self.white_queen()

        # for white king
        elif self.piece_to_move == 'wK':
            self.white_king()

        # for white pawn
        elif self.piece_to_move == 'wP':
            self.white_pawn()

        # for black rook 
        elif self.piece_to_move == 'bR':
            self.black_rook()

        # for black knight
        elif self.piece_to_move == 'bN':
            self.black_knight()

        # for black bishop
        elif self.piece_to_move == 'bB':
            self.black_bishop()

        # for black queen
        elif self.piece_to_move == 'bQ':
            self.black_queen()

        # for black king
        elif self.piece_to_move == 'bK':
            self.black_king()

        # for black pawn
        elif self.piece_to_move == 'bP':
            self.black_pawn()

        # incase something goes wrong
        else:
            pass

        return self.valid_moves


    def white_rook(self):
        """calculating all the possible moves for the white rook"""
        file = self.index_of_piece[0]   # get the file in which the rook is present (a, b, g...)
        rank = self.index_of_piece[1]   # get the rank in which the rook is present (1, 2, 7...)

        # change their order from string so that we can perform operation on them
        file = ord(file)    # ord() is to get the ascii value of the character
        rank = int(rank)

        while rank < 8:    # check all the possible moves upwards
            rank += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'w':  # if any white piece is present on the way, stop there
                    break
                else:       # if any black piece is present on the way, count that square too because we may take the black piece and then stop looking ahead
                    self.valid_moves.append(new_index)
                    break
            else:   # if nothing is on the way, keep moving and count the squares until we reach the 8th rank
                self.valid_moves.append(new_index)
        
        # after calculation reset the value to calculate in the other direction
        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)

        while rank > 1:     # check all the possible moves downwards
            rank -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] == 'w':  
                    break
                else:
                    self.valid_moves.append(new_index)
                    break
            else: 
                self.valid_moves.append(new_index)

        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)

        while file < 104:  # check all the possible moves to the right [104 is the ascii value of h]
            file += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] == 'w':  
                    break
                else:    
                    self.valid_moves.append(new_index)
                    break
            else:   
                self.valid_moves.append(new_index)

        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)

        while file > 97:   # check all the possible moves to the left [97 is the ascii value of a]
            file -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] == 'w':  
                    break
                else:       
                    self.valid_moves.append(new_index)
                    break
            else: 
                self.valid_moves.append(new_index)


    def black_rook(self):
        """calculating all the possible moves for the black rook"""
        file = self.index_of_piece[0]   # get the file in which the rook is present (a, b, g...)
        rank = self.index_of_piece[1]   # get the rank in which the rook is present (1, 2, 7...)

        # change their order from string so that we can perform operation on them
        file = ord(file)    # ord() is to get the ascii value of the character
        rank = int(rank)

        while rank < 8:    # check all the possible moves upwards
            rank += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'b':  # if any black piece is present on the way, stop there
                    break
                else:       # if any white piece is present on the way, count that square too because we may take the white piece and then stop looking ahead
                    self.valid_moves.append(new_index)
                    break
            else:   # if nothing is on the way, keep moving and count the squares until we reach the 8th rank
                self.valid_moves.append(new_index)
        
        # after calculation reset the value to calculate in the other direction
        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)

        while rank > 1:     # check all the possible moves downwards
            rank -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] == 'b':
                    break
                else:      
                    self.valid_moves.append(new_index)
                    break
            else:
                self.valid_moves.append(new_index)

        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)

        while file < 104:  # check all the possible moves to the right [104 is the ascii value of h]
            file += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] == 'b':  
                    break
                else:      
                    self.valid_moves.append(new_index)
                    break
            else:   
                self.valid_moves.append(new_index)

        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)

        while file > 97:  # check all the possible moves to the left [97 is the ascii value of a]
            file -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] == 'b': 
                    break
                else:      
                    self.valid_moves.append(new_index)
                    break
            else:   
                self.valid_moves.append(new_index)


    def white_bishop(self):
        """calculating all the possible moves for the white bishop"""
        file = self.index_of_piece[0]   # get the file in which the bishop is present (a, b, g...)
        rank = self.index_of_piece[1]   # get the rank in which the bishop is present (1, 2, 7...)

        # change their order from string so that we can perform operation on them
        file = ord(file)    # ord() is to get the ascii value of the character
        rank = int(rank)

        while rank < 8 and file < 104:  # check all the possible moves upward-right
            rank += 1 
            file += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'w':  # if any white piece is present on the way, stop there
                    break
                else:       # if any black piece is present on the way, count that square too because we may take the black piece and then stop looking ahead
                    self.valid_moves.append(new_index)
                    break
            else:   # if nothing is on the way, keep moving and count the squares until we reach the 8th rank or h file...whichever before
                self.valid_moves.append(new_index)

        # after calculation reset the value to calculate in the other direction
        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)


        while rank > 1 and file < 104:  # check all the possible moves downward-right
            rank -= 1
            file += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'w': 
                    break
                else:      
                    self.valid_moves.append(new_index)
                    break
            else:  
                self.valid_moves.append(new_index)

              
        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)


        while rank < 8 and file > 97:   # check all the possible moves upward-left
            rank += 1
            file -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'w': 
                    break
                else:      
                    self.valid_moves.append(new_index)
                    break
            else:  
                self.valid_moves.append(new_index)

              
        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank) 


        while rank > 1 and file > 97:   # check all the possible moves downward-left
            rank -= 1
            file -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'w': 
                    break
                else:      
                    self.valid_moves.append(new_index)
                    break
            else:  
                self.valid_moves.append(new_index)


    def black_bishop(self):
        """calculating all the possible moves for the black bishop"""
        file = self.index_of_piece[0]   # get the file in which the bishop is present (a, b, g...)
        rank = self.index_of_piece[1]   # get the rank in which the bishop is present (1, 2, 7...)

        # change their order from string so that we can perform operation on them
        file = ord(file)    # ord() is to get the ascii value of the character
        rank = int(rank)

        while rank < 8 and file < 104:  # check all the possible moves upward-right
            rank += 1 
            file += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'b':  # if any black piece is present on the way, stop there
                    break
                else:       # if any white piece is present on the way, count that square too because we may take the white piece and then stop looking ahead
                    self.valid_moves.append(new_index)
                    break
            else:   # if nothing is on the way, keep moving and count the squares until we reach the 8th rank or h file...whichever before
                self.valid_moves.append(new_index)

        # after calculation reset the value to calculate in the other direction
        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)


        while rank > 1 and file < 104:  # check all the possible moves downward-right
            rank -= 1
            file += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'b': 
                    break
                else:      
                    self.valid_moves.append(new_index)
                    break
            else:  
                self.valid_moves.append(new_index)

              
        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)


        while rank < 8 and file > 97:   # check all the possible moves upward-left
            rank += 1
            file -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'b': 
                    break
                else:      
                    self.valid_moves.append(new_index)
                    break
            else:  
                self.valid_moves.append(new_index)

              
        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank) 


        while rank > 1 and file > 97:   # check all the possible moves downward-left
            rank -= 1
            file -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'b': 
                    break
                else:      
                    self.valid_moves.append(new_index)
                    break
            else:  
                self.valid_moves.append(new_index)


    def white_king(self):
        """calculating all the possible moves for the white king"""
        file = self.index_of_piece[0]   # get the file in which the king is present (a, b, g...)
        rank = self.index_of_piece[1]   # get the rank in which the king is present (1, 2, 7...)

        # change their order from string so that we can perform operation on them
        file = ord(file)    # ord() is to get the ascii value of the character
        rank = int(rank)


        # for upward
        if rank < 8:
            rank += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:   # check if there is some piece on the new index
                if self.position[new_index][0] != 'w':  # make sure that the piece is not white, if it is not white append it to the list of the valid moves
                    self.valid_moves.append(new_index)
            else:        # if no piece is on the new index, append it to the list of valid moves
                self.valid_moves.append(new_index)

            # reset the index values
            file = self.index_of_piece[0]
            rank = self.index_of_piece[1]
            file = ord(file)
            rank = int(rank) 


        # for upward-right
        if rank < 8 and file < 104:
            rank += 1
            file += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] != 'w':
                    self.valid_moves.append(new_index)
            else:        
                self.valid_moves.append(new_index)
            
            # reset the index values
            file = self.index_of_piece[0]
            rank = self.index_of_piece[1]
            file = ord(file)
            rank = int(rank) 


        # for right
        if file < 104:
            file += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] != 'w':
                    self.valid_moves.append(new_index)
            else:        
                self.valid_moves.append(new_index)
            
            # reset the index values
            file = self.index_of_piece[0]
            rank = self.index_of_piece[1]
            file = ord(file)
            rank = int(rank) 


        # for downward-right
        if rank > 1 and file < 104:
            rank -= 1 
            file += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] != 'w':
                    self.valid_moves.append(new_index)
            else:        
                self.valid_moves.append(new_index)
            
            # reset the index values
            file = self.index_of_piece[0]
            rank = self.index_of_piece[1]
            file = ord(file)
            rank = int(rank) 


        # for downward
        if rank > 1:
            rank -= 1 
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] != 'w':
                    self.valid_moves.append(new_index)
            else:        
                self.valid_moves.append(new_index)
            
            # reset the index values
            file = self.index_of_piece[0]
            rank = self.index_of_piece[1]
            file = ord(file)
            rank = int(rank) 


        # for downward-left
        if rank > 1 and file > 97:
            rank -= 1 
            file -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] != 'w':
                    self.valid_moves.append(new_index)
            else:        
                self.valid_moves.append(new_index)
            
            # reset the index values
            file = self.index_of_piece[0]
            rank = self.index_of_piece[1]
            file = ord(file)
            rank = int(rank) 


        # for left 
        if file > 97:
            file -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] != 'w':
                    self.valid_moves.append(new_index)
            else:        
                self.valid_moves.append(new_index)
            
            # reset the index values
            file = self.index_of_piece[0]
            rank = self.index_of_piece[1]
            file = ord(file)
            rank = int(rank) 


        # for upward-left 
        if rank < 8 and file > 97:
            rank += 1
            file -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] != 'w':
                    self.valid_moves.append(new_index)
            else:        
                self.valid_moves.append(new_index)
        
            # reset the index values
            file = self.index_of_piece[0]
            rank = self.index_of_piece[1]
            file = ord(file)
            rank = int(rank) 


    def black_king(self):
        """calculating all the possible moves for the black king"""
        file = self.index_of_piece[0]   # get the file in which the king is present (a, b, g...)
        rank = self.index_of_piece[1]   # get the rank in which the king is present (1, 2, 7...)

        # change their order from string so that we can perform operation on them
        file = ord(file)    # ord() is to get the ascii value of the character
        rank = int(rank)


        # for upward
        if rank < 8:
            rank += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:   # check if there is some piece on the new index
                if self.position[new_index][0] != 'b':  # make sure that the piece is not black, if it is not black append it to the list of the valid moves
                    self.valid_moves.append(new_index)
            else:        # if no piece is on the new index, append it to the list of valid moves
                self.valid_moves.append(new_index)

            # reset the index values
            file = self.index_of_piece[0]
            rank = self.index_of_piece[1]
            file = ord(file)
            rank = int(rank) 


        # for upward-right
        if rank < 8 and file < 104:
            rank += 1
            file += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] != 'b':
                    self.valid_moves.append(new_index)
            else:        
                self.valid_moves.append(new_index)
            
            # reset the index values
            file = self.index_of_piece[0]
            rank = self.index_of_piece[1]
            file = ord(file)
            rank = int(rank) 


        # for right
        if file < 104:
            file += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] != 'b':
                    self.valid_moves.append(new_index)
            else:        
                self.valid_moves.append(new_index)
            
            # reset the index values
            file = self.index_of_piece[0]
            rank = self.index_of_piece[1]
            file = ord(file)
            rank = int(rank) 


        # for downward-right
        if rank > 1 and file < 104:
            rank -= 1 
            file += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] != 'b':
                    self.valid_moves.append(new_index)
            else:        
                self.valid_moves.append(new_index)
            
            # reset the index values
            file = self.index_of_piece[0]
            rank = self.index_of_piece[1]
            file = ord(file)
            rank = int(rank) 


        # for downward
        if rank > 1:
            rank -= 1 
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] != 'b':
                    self.valid_moves.append(new_index)
            else:        
                self.valid_moves.append(new_index)
            
            # reset the index values
            file = self.index_of_piece[0]
            rank = self.index_of_piece[1]
            file = ord(file)
            rank = int(rank) 


        # for downward-left
        if rank > 1 and file > 97:
            rank -= 1 
            file -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] != 'b':
                    self.valid_moves.append(new_index)
            else:        
                self.valid_moves.append(new_index)
            
            # reset the index values
            file = self.index_of_piece[0]
            rank = self.index_of_piece[1]
            file = ord(file)
            rank = int(rank) 


        # for left 
        if file > 97:
            file -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] != 'b':
                    self.valid_moves.append(new_index)
            else:        
                self.valid_moves.append(new_index)
            
            # reset the index values
            file = self.index_of_piece[0]
            rank = self.index_of_piece[1]
            file = ord(file)
            rank = int(rank) 


        # for upward-left 
        if rank < 8 and file > 97:
            rank += 1
            file -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] != 'b':
                    self.valid_moves.append(new_index)
            else:        
                self.valid_moves.append(new_index)
        
            # reset the index values
            file = self.index_of_piece[0]
            rank = self.index_of_piece[1]
            file = ord(file)
            rank = int(rank) 


    def white_queen(self):
        """calculating all the possible moves for the white queen"""
        file = self.index_of_piece[0]   # get the file in which the queen is present (a, b, g...)
        rank = self.index_of_piece[1]   # get the rank in which the queen is present (1, 2, 7...)

        # change their order from string so that we can perform operation on them
        file = ord(file)    # ord() is to get the ascii value of the character
        rank = int(rank)


        while rank < 8:    # check all the possible moves upwards
            rank += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'w':  # if any white piece is present on the way, stop there
                    break
                else:       # if any black piece is present on the way, count that square too because we may take the black piece and then stop looking ahead
                    self.valid_moves.append(new_index)
                    break
            else:   # if nothing is on the way, keep moving and count the squares until we reach the 8th rank
                self.valid_moves.append(new_index)
        
        # after calculation reset the value to calculate in the other direction
        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)


        while rank < 8 and file < 104:  # check all the possible moves upward-right
            rank += 1 
            file += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'w':  # if any white piece is present on the way, stop there
                    break
                else:       # if any black piece is present on the way, count that square too because we may take the black piece and then stop looking ahead
                    self.valid_moves.append(new_index)
                    break
            else:   # if nothing is on the way, keep moving and count the squares until we reach the 8th rank or h file...whichever before
                self.valid_moves.append(new_index)

        # after calculation reset the value to calculate in the other direction
        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)


        while file < 104:  # check all the possible moves to the right [104 is the ascii value of h]
            file += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] == 'w':  
                    break
                else:    
                    self.valid_moves.append(new_index)
                    break
            else:   
                self.valid_moves.append(new_index)

        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)

        
        while rank > 1 and file < 104:  # check all the possible moves downward-right
            rank -= 1
            file += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'w': 
                    break
                else:      
                    self.valid_moves.append(new_index)
                    break
            else:  
                self.valid_moves.append(new_index)

              
        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)


        while rank > 1:     # check all the possible moves downwards
            rank -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] == 'w':  
                    break
                else:
                    self.valid_moves.append(new_index)
                    break
            else: 
                self.valid_moves.append(new_index)

        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)


        while rank > 1 and file > 97:   # check all the possible moves downward-left
            rank -= 1
            file -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'w': 
                    break
                else:      
                    self.valid_moves.append(new_index)
                    break
            else:  
                self.valid_moves.append(new_index)

        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)


        while file > 97:   # check all the possible moves to the left [97 is the ascii value of a]
            file -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] == 'w':  
                    break
                else:       
                    self.valid_moves.append(new_index)
                    break
            else: 
                self.valid_moves.append(new_index)
            
        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)

        while rank < 8 and file > 97:   # check all the possible moves upward-left
            rank += 1
            file -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'w': 
                    break
                else:      
                    self.valid_moves.append(new_index)
                    break
            else:  
                self.valid_moves.append(new_index)


    def black_queen(self):
        """calculating all the possible moves for the black queen"""
        file = self.index_of_piece[0]   # get the file in which the queen is present (a, b, g...)
        rank = self.index_of_piece[1]   # get the rank in which the queen is present (1, 2, 7...)

        # change their order from string so that we can perform operation on them
        file = ord(file)    # ord() is to get the ascii value of the character
        rank = int(rank)


        while rank < 8:    # check all the possible moves upwards
            rank += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'b':  # if any black piece is present on the way, stop there
                    break
                else:       # if any white piece is present on the way, count that square too because we may take the white piece and then stop looking ahead
                    self.valid_moves.append(new_index)
                    break
            else:   # if nothing is on the way, keep moving and count the squares until we reach the 8th rank
                self.valid_moves.append(new_index)
        
        # after calculation reset the value to calculate in the other direction
        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)


        while rank < 8 and file < 104:  # check all the possible moves upward-right
            rank += 1 
            file += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'b':  # if any black piece is present on the way, stop there
                    break
                else:       # if any white piece is present on the way, count that square too because we may take the white piece and then stop looking ahead
                    self.valid_moves.append(new_index)
                    break
            else:   # if nothing is on the way, keep moving and count the squares until we reach the 8th rank or h file...whichever before
                self.valid_moves.append(new_index)

        # after calculation reset the value to calculate in the other direction
        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)


        while file < 104:  # check all the possible moves to the right [104 is the ascii value of h]
            file += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] == 'b':  
                    break
                else:    
                    self.valid_moves.append(new_index)
                    break
            else:   
                self.valid_moves.append(new_index)

        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)

        
        while rank > 1 and file < 104:  # check all the possible moves downward-right
            rank -= 1
            file += 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'b': 
                    break
                else:      
                    self.valid_moves.append(new_index)
                    break
            else:  
                self.valid_moves.append(new_index)

              
        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)


        while rank > 1:     # check all the possible moves downwards
            rank -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] == 'b':  
                    break
                else:
                    self.valid_moves.append(new_index)
                    break
            else: 
                self.valid_moves.append(new_index)

        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)


        while rank > 1 and file > 97:   # check all the possible moves downward-left
            rank -= 1
            file -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'b': 
                    break
                else:      
                    self.valid_moves.append(new_index)
                    break
            else:  
                self.valid_moves.append(new_index)

        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)


        while file > 97:   # check all the possible moves to the left [97 is the ascii value of a]
            file -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:
                if self.position[new_index][0] == 'b':  
                    break
                else:       
                    self.valid_moves.append(new_index)
                    break
            else: 
                self.valid_moves.append(new_index)
            
        file = self.index_of_piece[0]
        rank = self.index_of_piece[1]
        file = ord(file)
        rank = int(rank)

        while rank < 8 and file > 97:   # check all the possible moves upward-left
            rank += 1
            file -= 1
            new_index = f"{chr(file)}{rank}"
            if new_index in self.position:  
                if self.position[new_index][0] == 'b': 
                    break
                else:      
                    self.valid_moves.append(new_index)
                    break
            else:  
                self.valid_moves.append(new_index)

    
    def white_pawn(self):
        """calculating all the possible moves for the white pawn"""

        file = self.index_of_piece[0]   # get the file in which the pawn is present (a, b, g...)
        rank = self.index_of_piece[1]   # get the rank in which the pawn is present (1, 2, 7...)

        # change their order from string so that we can perform operation on them
        file = ord(file)    # ord() is to get the ascii value of the character
        rank = int(rank)

        
        if file < 104:   # to check whether it can move diagonally right
            new_index = f"{chr(file + 1)}{rank + 1}"
            if new_index in self.position and self.position[new_index][0] == 'b':   # if there's a black piece to the diagonally right of the pawn
                self.valid_moves.append(new_index)

        if file > 97:   # to check whether it can move diagonally left
            new_index = f"{chr(file - 1)}{rank + 1}"
            if new_index in self.position and self.position[new_index][0] == 'b':   # if there's a black piece to the diagonally left of the pawn
                self.valid_moves.append(new_index)

        # for the first move, when it can move one/two square at a time
        if rank == 2:
            new_index = f"{chr(file)}{rank + 1}"    # to check if it can move one square, by making sure that no other piece is ahead of it
            if new_index not in self.position:
                self.valid_moves.append(new_index)  


                new_index = f"{chr(file)}{rank + 2}"     # check if it can move second square
                if new_index not in self.position:
                    self.valid_moves.append(new_index)

        # for other moves when it can move only one square
        elif rank < 8:
            new_index = f"{chr(file)}{rank + 1}"
            if new_index not in self.position:
                self.valid_moves.append(new_index)

    
    def black_pawn(self):
        """calculating all the possible moves for the black pawn"""

        file = self.index_of_piece[0]   # get the file in which the pawn is present (a, b, g...)
        rank = self.index_of_piece[1]   # get the rank in which the pawn is present (1, 2, 7...)

        # change their order from string so that we can perform operation on them
        file = ord(file)    # ord() is to get the ascii value of the character
        rank = int(rank)

        
        if file < 104:   # to check whether it can move diagonally right
            new_index = f"{chr(file + 1)}{rank - 1}"
            if new_index in self.position and self.position[new_index][0] == 'w':   # if there's a white piece to the diagonally right of the pawn
                self.valid_moves.append(new_index)

        if file > 97:   # to check whether it can move diagonally left
            new_index = f"{chr(file - 1)}{rank - 1}"
            if new_index in self.position and self.position[new_index][0] == 'w':   # if there's a white piece to the diagonally left of the pawn
                self.valid_moves.append(new_index)

        # for the first move, when it can move one/two square at a time
        if rank == 7:
            new_index = f"{chr(file)}{rank - 1}"    # to check if it can move one square, by making sure that no other piece is ahead of it
            if new_index not in self.position:
                self.valid_moves.append(new_index)  


                new_index = f"{chr(file)}{rank - 2}"     # check if it can move second square
                if new_index not in self.position:
                    self.valid_moves.append(new_index)

        # for other moves when it can move only one square
        elif rank > 1:
            new_index = f"{chr(file)}{rank - 1}"
            if new_index not in self.position:
                self.valid_moves.append(new_index)


    def white_knight(self):
        """calculating all the possible moves for the white knight"""
        file = self.index_of_piece[0]   # get the file in which the knight is present (a, b, g...)
        rank = self.index_of_piece[1]   # get the rank in which the knight is present (1, 2, 7...)

        # change their order from string so that we can perform operation on them
        file = ord(file)    # ord() is to get the ascii value of the character
        rank = int(rank)


        # for upward-right
        if (rank + 2) <= 8 and (file + 1) <= 104:   # if the square is valid
            new_index = f"{chr(file + 1)}{rank + 2}"
            if new_index in self.position:  # check whether there is some piece in the square
                if self.position[new_index][0] == 'b':  # append the square in the list of valid moves only if there is a black piece on the square
                    self.valid_moves.append(new_index)
            else:      # if there is no piece on the square, append it anyway
                self.valid_moves.append(new_index)

        # for right-upward
        if (rank + 1) <= 8 and (file + 2) <= 104:
            new_index = f"{chr(file + 2)}{rank + 1}"
            if new_index in self.position:
                if self.position[new_index][0] == 'b': 
                    self.valid_moves.append(new_index)
            else: 
                self.valid_moves.append(new_index)

        # for right-downward
        if (rank - 1) >= 1 and (file + 2) <= 104:
            new_index = f"{chr(file + 2)}{rank - 1}"
            if new_index in self.position:
                if self.position[new_index][0] == 'b': 
                    self.valid_moves.append(new_index)
            else: 
                self.valid_moves.append(new_index)

        # for downward-right
        if (rank - 2) >= 1 and (file + 1) <= 104:
            new_index = f"{chr(file + 1)}{rank - 2}"
            if new_index in self.position:
                if self.position[new_index][0] == 'b': 
                    self.valid_moves.append(new_index)
            else: 
                self.valid_moves.append(new_index)

        # for downward-left
        if (rank - 2) >= 1 and (file - 1) >= 97:
            new_index = f"{chr(file - 1)}{rank - 2}"
            if new_index in self.position:
                if self.position[new_index][0] == 'b': 
                    self.valid_moves.append(new_index)
            else: 
                self.valid_moves.append(new_index)

        # for left-downward
        if (rank - 1) >= 1 and (file - 2) >= 97:
            new_index = f"{chr(file - 2)}{rank - 1}"
            if new_index in self.position:
                if self.position[new_index][0] == 'b': 
                    self.valid_moves.append(new_index)
            else: 
                self.valid_moves.append(new_index)

        # for left-upward
        if (rank + 1) <= 8 and (file - 2) >= 97:
            new_index = f"{chr(file - 2)}{rank + 1}"
            if new_index in self.position:
                if self.position[new_index][0] == 'b': 
                    self.valid_moves.append(new_index)
            else: 
                self.valid_moves.append(new_index)

        # for upward-left
        if (rank + 2) <= 8 and (file - 1) >= 97:
            new_index = f"{chr(file - 1)}{rank + 2}"
            if new_index in self.position:
                if self.position[new_index][0] == 'b': 
                    self.valid_moves.append(new_index)
            else: 
                self.valid_moves.append(new_index)


    def black_knight(self):
        """calculating all the possible moves for the black knight"""
        file = self.index_of_piece[0]   # get the file in which the knight is present (a, b, g...)
        rank = self.index_of_piece[1]   # get the rank in which the knight is present (1, 2, 7...)

        # change their order from string so that we can perform operation on them
        file = ord(file)    # ord() is to get the ascii value of the character
        rank = int(rank)


        # for upward-right
        if (rank + 2) <= 8 and (file + 1) <= 104:   # if the square is valid
            new_index = f"{chr(file + 1)}{rank + 2}"
            if new_index in self.position:  # check whether there is some piece in the square
                if self.position[new_index][0] == 'w':  # append the square in the list of valid moves only if there is a white piece on the square
                    self.valid_moves.append(new_index)
            else:      # if there is no piece on the square, append it anyway
                self.valid_moves.append(new_index)

        # for right-upward
        if (rank + 1) <= 8 and (file + 2) <= 104:
            new_index = f"{chr(file + 2)}{rank + 1}"
            if new_index in self.position:
                if self.position[new_index][0] == 'w': 
                    self.valid_moves.append(new_index)
            else: 
                self.valid_moves.append(new_index)

        # for right-downward
        if (rank - 1) >= 1 and (file + 2) <= 104:
            new_index = f"{chr(file + 2)}{rank - 1}"
            if new_index in self.position:
                if self.position[new_index][0] == 'w': 
                    self.valid_moves.append(new_index)
            else: 
                self.valid_moves.append(new_index)

        # for downward-right
        if (rank - 2) >= 1 and (file + 1) <= 104:
            new_index = f"{chr(file + 1)}{rank - 2}"
            if new_index in self.position:
                if self.position[new_index][0] == 'w': 
                    self.valid_moves.append(new_index)
            else: 
                self.valid_moves.append(new_index)

        # for downward-left
        if (rank - 2) >= 1 and (file - 1) >= 97:
            new_index = f"{chr(file - 1)}{rank - 2}"
            if new_index in self.position:
                if self.position[new_index][0] == 'w': 
                    self.valid_moves.append(new_index)
            else: 
                self.valid_moves.append(new_index)

        # for left-downward
        if (rank - 1) >= 1 and (file - 2) >= 97:
            new_index = f"{chr(file - 2)}{rank - 1}"
            if new_index in self.position:
                if self.position[new_index][0] == 'w': 
                    self.valid_moves.append(new_index)
            else: 
                self.valid_moves.append(new_index)

        # for left-upward
        if (rank + 1) <= 8 and (file - 2) >= 97:
            new_index = f"{chr(file - 2)}{rank + 1}"
            if new_index in self.position:
                if self.position[new_index][0] == 'w': 
                    self.valid_moves.append(new_index)
            else: 
                self.valid_moves.append(new_index)

        # for upward-left
        if (rank + 2) <= 8 and (file - 1) >= 97:
            new_index = f"{chr(file - 1)}{rank + 2}"
            if new_index in self.position:
                if self.position[new_index][0] == 'w': 
                    self.valid_moves.append(new_index)
            else: 
                self.valid_moves.append(new_index)

        