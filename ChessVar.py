# Author: Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 11/26/2023
# Description: Defines a class named ChessVar for playing an abstract board game that is a variant of chess.
# Defines a pieces class to store information on various pieces that are on the chess board.

"""
----------------------------DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS-----------------------------------


1. TODO Initializing the ChessVar class


The ChessVar class contains five data members. They will be initialized as follows:
The board data member will be initialized to a dictionary with each possible position as a key.
Chess piece objects, with a color and kind, will be the values for these keys. When the board data member is initialized
the keys for rows 3-6 ('a3' - 'h6') will hold the value None, as no chess piece starts there. Other keys will have a
value that is a piece object, with the type of piece and color being determined by the key in question. For example, the
key 'a1' will have a value that is a Piece object with kind set to 'Castle' and color set to 'White' as a white castle
always starts at square a1 in a game of chess.

The turn data member will be initialized to 'White' as white always takes the first turn in chess.

The whites and blacks data members will be initialized to dictionaries that reflect all the pieces on the board for
whites and blacks, respectively, at the start of the game. Per the rules of chess, both whites and blacks start with
{'Castle': 2, 'Knight': 2, 'Bishop': 2, 'King': 1, 'Queen': 1, 'Pawn': 8}. This gives us a way to track when any of the
keys (types/kinds of pieces) reach 0 pieces on the board. This is when the player without any type/kind of pieces at 0
wins.

The game state data member will be initialized to 'UNFINISHED' as all chess games begin as unfinished. This data
member is updated when a player reaches a win condition.


2. TODO Keeping track of turn order


The turn order will be tracked with a data member in the ChessVar class, specifically the turn data member. The turn
data member will be initialized to 'White' and oscillate between 'Black' and 'White'. Once the white player completes a
valid move, the next_move method in the ChessVar class will be called on the ChessVar object. If the turn data member is
white, it will change the turn data member to black. If the turn data member is black, it will change the turn data
member to white. Once a win condition is achieved, the game state data member is updated to 'WHITE_WON' or 'BLACK_WON'.

I considered updating the turn to None once the win condition is achieved, but since I already update the game state
data member, this is superfluous.


3. TODO Keeping track of the current board position


The ChessVar class is responsible for keeping track of the current board position using the board data member.
The board data member will be initialized to a dictionary with each possible position as a key.
None or a chess piece objects, with a color and kind, will be the values for these keys. When initialized, only
positions that start the game with a piece on them will have a value with a chess piece object.
Whenever a move is completed using the make_move method, two updates to the board data member will occur:
First, the value for the current position of the piece being moved (key) will be set to None, as there is no piece at
the position once the current piece is moved. Secondly, the value of the new position (key) will be updated to hold the
chess piece object that we just moved. This will change the previous value for that position key from either None or
a different chess piece object, depending on if the position was empty or occupied by an opposing player's piece.
Updating the board data member's dictionary after each move will allow it to accurately track the current board
position.


4. TODO Determining if a regular move is valid


The make_move method in the ChessVar class will perform a series of checks to determine if the move is valid,
before calling a piece specific move method which will perform the final validity checks.
The make_move method in the ChessVar class will take the current position and desired position as parameters then:
1. Check the game state data member to see if the game is still unfinished
    if game state == 'WHITE_WON' or 'BLACK_WON', return False
2. Check the current and desired positions to ensure they are both on the board (in the board data member dictionary)
    if current position not in board or desired position not in board, return False
3. Check that the piece at the starting position is the same color as the turn data member
    if board[starting position].get_color() != turn, return False
4. Check that the piece at the desired position is empty or does not have the same color as the turn data member
    if board[desired position].get_color() == turn, return False
5. If False has not yet been returned then call a move method for a specific piece (like move_castle or move_pawn),
passing the current and desired position as parameters.
The move_specific_piece method (move_queen, move_king, etc.) will take current and desired position as parameters then:
1. Initialize an empty list of possible moves.
    possible moves = []
2. Depending on the specific piece:
    a. add all possible moves upwards (if pawn, castle, knight, queen, king)
        - Check if the next space in that direction is blocked by a piece of the same color (unless knight)
        - add next space to possible moves if not blocked
        - Check if the next space in that direction is blocked by a piece of the opposing color (unless knight)
        - add next space to possible moves and end repeat
        - repeat until blocked or limited by piece's movement ability
    b. add all possible moves to the upper-right diagonal (if bishop, queen, pawn, king)
        - Check if the next space in that direction is blocked by a piece of the same color (unless knight)
        - add next space to possible moves if not blocked
        - Check if the next space in that direction is blocked by a piece of the opposing color (unless knight)
        - add next space to possible moves and end repeat
        - repeat until blocked or limited by piece's movement ability
    c. add all possible moves to the right (if castle, knight, king, queen)
        - Check if the next space in that direction is blocked by a piece of the same color (unless knight)
        - add next space to possible moves if not blocked
        - Check if the next space in that direction is blocked by a piece of the opposing color (unless knight)
        - add next space to possible moves and end repeat
        - repeat until blocked or limited by piece's movement ability
    d. add all possible moves to the lower-right diagonal (if bishop, queen, king)
        - Check if the next space in that direction is blocked by a piece of the same color (unless knight)
        - add next space to possible moves if not blocked
        - Check if the next space in that direction is blocked by a piece of the opposing color (unless knight)
        - add next space to possible moves and end repeat
        - repeat until blocked or limited by piece's movement ability
    e. add all possible moves downwards (if castle, knight, queen, king)
        - Check if the next space in that direction is blocked by a piece of the same color (unless knight)
        - add next space to possible moves if not blocked
        - Check if the next space in that direction is blocked by a piece of the opposing color (unless knight)
        - add next space to possible moves and end repeat
        - repeat until blocked or limited by piece's movement ability
    f. add all possible moves to the lower-left diagonal (if bishop, queen, king)
        - Check if the next space in that direction is blocked by a piece of the same color (unless knight)
        - add next space to possible moves if not blocked
        - Check if the next space in that direction is blocked by a piece of the opposing color (unless knight)
        - add next space to possible moves and end repeat
        - repeat until blocked or limited by piece's movement ability
    g. add all possible moves to the left (if castle, knight, king, queen)
        - Check if the next space in that direction is blocked by a piece of the same color (unless knight)
        - add next space to possible moves if not blocked
        - Check if the next space in that direction is blocked by a piece of the opposing color (unless knight)
        - add next space to possible moves and end repeat
        - repeat until blocked or limited by piece's movement ability
    h. add all possible moves to the upper-left diagonal (if bishop, queen, pawn, king)
        - Check if the next space in that direction is blocked by a piece of the same color (unless knight)
        - add next space to possible moves if not blocked
        - Check if the next space in that direction is blocked by a piece of the opposing color (unless knight)
        - add next space to possible moves and end repeat
        - repeat until blocked or limited by piece's movement ability
3. Check if desired position is in possible positions
    if desired position not in possible positions:
4. If not in possible positions, do not update position and return False.
    return False
5. If it is in possible positions
    else:
6. Check if an opposing piece is there:
    if board[desired position] is None:
7. If no piece is there, update board data member current position key to none and desired position key to the chess
piece object that was at current position. Then return True.
    board[desired position] = board[current position]
    board[current position] = none
    return True
8. If there is a piece there, then call the capture_piece method and pass the desired position as a parameter.
then update board data member current position key to none and desired position key to the chess
piece object that was at current position. Then return True.
    self.capture_piece(desired position)
    board[desired position] = board[current position]
    board[current position] = none
    return True
The capture piece method for the Chess Var class takes the desired position as a parameter then:
1. Identifies the type and color of the piece to at the desired position
2. Lowers a value in the whites or blacks data members dictionary based on the piece color and type
3. Checks if the type/kind of piece that was captured is not on the board
4. Updates the game state if the last piece of its kind was captured


5. TODO Determining if a capture is valid

I treat capture as a specific type of move, so the actionable plan for validating captures is included above.
This is covered in my processes for determining if a move is valid and is detailed in pseudocode above from line 68-154.
I will summarize below, but please see lines 68-154 if more info is needed.
For brevity I do not wish to re-paste it here.

The move method for a specific piece will create a list of all possible moves, including moves that capture opposing
pieces. Only moves that are not blocked (except for knights) and end at a position that is empty or occupied by a piece
of a different color can be added to the list of possible moves. Hence, the move method for a specific piece will
create a list containing all valid captures. The move method for a specific piece will then check if the desired move
is a capture and call the capture piece method before updating the board to reflect the outcome of the move.

The capture piece method for the Chess Var class occurs after validation and takes the desired position as a parameter
then:
1. Identifies the type and color of the piece to at the desired position
2. Lowers a value in the whites or blacks data members dictionary based on the piece color and type
3. Checks if the type/kind of piece that was captured is not on the board
4. Updates the game state if the last piece of its kind was captured


6. TODO Determining the current state of the game


The current state of the game is tracked by the game state data member.
The game state data member is initialized to 'UNFINISHED'
As the state of the game can only change when a piece is taken, I use the capture piece method to determine the current
state of the game.

The capture piece method is called whenever a player makes a valid move with a piece of their color
to a desired position with a piece of the opposing color.
The capture piece method for the Chess Var class then takes the desired position as a parameter and:
1. Identifies the type and color of the piece to at the desired position
        captured_piece = self._board[piece_pos].get_kind()
        captured_color = self._board[piece_pos].get_color()
2. Lowers a value in the whites or blacks data members dictionary based on the piece color and type
        if captured_color == 'Black':
            self._blacks[captured_piece] -= 1
        else:
            self._whites[captured_piece] -= 1
3. Checks if the type/kind of piece that was captured is not on the board
            if self._blacks[captured_piece] < 1:
4. Updates the game state if the last piece of its kind was captured
                self.set_game_state('WHITE_WON')

- You can see the completed capture_piece() method below to review the code.
"""


def letter_to_number(letter):
    """
    Converts a letter to a corresponding number representing a column on a chess board (1 being far left and
    8 being far right). Used to calculate new positions.
    :param letter: The letter we are converting
    :return: a number representing the column the letter represents (from left to right) on a chess board.
    Returns o if the letter does not correspond to a column on the chess board.
    """
    if letter == 'a':
        return 1
    if letter == 'b':
        return 2
    if letter == 'c':
        return 3
    if letter == 'd':
        return 4
    if letter == 'e':
        return 5
    if letter == 'f':
        return 6
    if letter == 'g':
        return 7
    if letter == 'h':
        return 8
    else:
        return 0


def number_to_letter(number):
    """
    Converts a number to a corresponding letter representing a column on a chess board (a being far left and
    h being far right). Used to calculate new positions.
    :param number: The number we are converting
    :return: a letter representing the column the number represents (from left to right) on a chess board.
    Returns z if the number does not correspond to a column on the chess board.
    """
    if number == 1:
        return 'a'
    if number == 2:
        return 'b'
    if number == 3:
        return 'c'
    if number == 4:
        return 'd'
    if number == 5:
        return 'e'
    if number == 6:
        return 'f'
    if number == 7:
        return 'g'
    if number == 8:
        return 'h'
    else:
        return 'z'


class Piece:
    """
    A class representing a chess piece on a chess board.
    Piece types/kinds include Castle, Knight, Bishop, Queen, King, and Pawn.
    Responsible only for storing the color and type/kind of each piece.
    This class communicates with the ChessVar class by making the type/kind and color of each piece accessible
    through its get_kind and get_color methods.
    """

    def __init__(self, kind, color):
        """
        Initializes the type of piece (kind) and the color of the piece
        """
        self._kind = kind
        self._color = color

    def get_kind(self):
        """
        Returns the type (kind) of piece using data member
        :return: A string stating type of piece (Castle, Knight, Bishop, Queen, King, or Pawn)
        """
        return self._kind

    def get_color(self):
        """
        Returns the color of a piece using data member
        :return: A string stating color of piece, 'White' or 'Black'
        """
        return self._color


class ChessVar:
    """
    A class representing a game of variant chess in which the first player to lose all pieces of any type loses.
    Win condition: When a player captures 1 King, 1 Queen, 8 Pawns, 2 Horses, 2 Bishops, or 2 Castles.
    This is the core class representing the game itself. It is responsible for:
    1. Tracking the positions of all pieces, using the board data member.
    2. Tracking whose turn it is to move a piece, using the turn data member
    3. Determining when the game has been won and by which player, using data members to track the remaining pieces for
    each player and then update the game state data member when the win condition is fulfilled.
    4. Implementing moves. Using a current and desired position the program will determine what piece is in the current
    position and if the piece can be moved by the current player. If it can be moved, the program will then determine
    if a move to the desired position is valid according to the current board arrangement and movement abilities of the
    piece.
    This class will communicate with the Piece class to retrieve the type/kind and color of pieces on the board
    """

    def __init__(self):
        """
        Initializes the board set up, the turn, the game state, and the pieces in play for both white and black.
        """
        self._board = {
            'a8': Piece('Castle', 'Black'), 'b8': Piece('Knight', 'Black'), 'c8': Piece('Bishop', 'Black'),
            'd8': Piece('Queen', 'Black'), 'e8': Piece('King', 'Black'), 'f8': Piece('Bishop', 'Black'),
            'g8': Piece('Knight', 'Black'), 'h8': Piece('Castle', 'Black'),
            'a7': Piece('Pawn', 'Black'), 'b7': Piece('Pawn', 'Black'), 'c7': Piece('Pawn', 'Black'),
            'd7': Piece('Pawn', 'Black'), 'e7': Piece('Pawn', 'Black'), 'f7': Piece('Pawn', 'Black'),
            'g7': Piece('Pawn', 'Black'), 'h7': Piece('Pawn', 'Black'),
            'a6': None, 'b6': None, 'c6': None, 'd6': None, 'e6': None, 'f6': None, 'g6': None, 'h6': None,
            'a5': None, 'b5': None, 'c5': None, 'd5': None, 'e5': None, 'f5': None, 'g5': None, 'h5': None,
            'a4': None, 'b4': None, 'c4': None, 'd4': None, 'e4': None, 'f4': None, 'g4': None, 'h4': None,
            'a3': None, 'b3': None, 'c3': None, 'd3': None, 'e3': None, 'f3': None, 'g3': None, 'h3': None,
            'a2': Piece('Pawn', 'White'), 'b2': Piece('Pawn', 'White'), 'c2': Piece('Pawn', 'White'),
            'd2': Piece('Pawn', 'White'), 'e2': Piece('Pawn', 'White'), 'f2': Piece('Pawn', 'White'),
            'g2': Piece('Pawn', 'White'), 'h2': Piece('Pawn', 'White'),
            'a1': Piece('Castle', 'White'), 'b1': Piece('Knight', 'White'), 'c1': Piece('Bishop', 'White'),
            'd1': Piece('Queen', 'White'), 'e1': Piece('King', 'White'), 'f1': Piece('Bishop', 'White'),
            'g1': Piece('Knight', 'White'), 'h1': Piece('Castle', 'White')
        }
        self._turn = 'White'
        self._whites = {'Castle': 2, 'Knight': 2, 'Bishop': 2, 'King': 1, 'Queen': 1, 'Pawn': 8}
        self._blacks = {'Castle': 2, 'Knight': 2, 'Bishop': 2, 'King': 1, 'Queen': 1, 'Pawn': 8}
        self._game_state = 'UNFINISHED'

    def next_turn(self):
        """
        Marks the end of a players turn. Changes the turn to the opposing player's turn.
        :return: None, updates the turn data member
        """
        # if the current turn is black, change to white
        if self._turn == 'Black':
            self._turn = 'White'
        # if current turn is white, change to black
        else:
            self._turn = 'Black'

    def capture_piece(self, piece_pos):
        """
        Represents the capturing of a chess piece by the opposing player.
        Takes a location on the board as a parameter and removes whatever piece was there.
        Updates the dictionary of pieces for the player (color) that is losing a piece to reflect the loss.
        If that was the last piece of its type/kind, then updates the game state to reflect whoever won.
        :param piece_pos: A string indicating the position the capturing player is moving their piece to,
         which is currently occupied by the opposing player.
        :return: None, updates the dictionary of player pieces and the game state if applicable
        """
        # set captured piece and color to the values for the piece being taken
        captured_piece = self._board[piece_pos].get_kind()
        captured_color = self._board[piece_pos].get_color()

        # if the captured piece is black, remove from blacks
        if captured_color == 'Black':
            self._blacks[captured_piece] -= 1
            # check if that was the last piece of its type/kind
            if self._blacks[captured_piece] < 1:
                self.set_game_state('WHITE_WON')

        # if the captured piece is white, remove from whites
        else:
            self._whites[captured_piece] -= 1
            # check if that was the last piece of its type/kind
            if self._whites[captured_piece] < 1:
                self.set_game_state('BLACK_WON')

    def set_game_state(self, new_game_state):
        """
        Updates the game state from 'UNFINISHED' to either 'WHITE_WON' or 'BLACK_WON'
        :param new_game_state: A string with the new game state
        :return: None, updates data member
        """
        self._game_state = new_game_state

    def get_game_state(self):
        """
        Checks the game state data member to determine if the game has been won yet
        :return: A string reflecting the game state, like 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'
        """
        return self._game_state

    def make_move(self, start_pos, end_pos):
        """
        Attempts to move the piece in the starting position (start_pos) to the desired position (end_pos).
        Returns true if the move was made and the board was updated. If the move was not possible than it returns False.
        Checks that the game is still unfinished, that both positions are on the board, that the piece at the starting
        position belongs to the player whose turn it is,
        and that the desired position is empty or occupied by a piece belonging to the opposing player.
        If all of these criteria are valid, the method calls the specific move method for the type/kind of piece.
        The specific move method then compiles a list of all possible moves based on the current board state, and
        determines if the desired move is possible.
        :param start_pos: A string representing the current position of the piece to be moved (like 'a7')
        :param end_pos: A string representing the desired position of the piece to be moved (like 'a6')
        :return: bool: True if move completed, False if not completed due to it being invalid
        """
        # Check the game state data member to see if the game is still unfinished
        if self.get_game_state() != 'UNFINISHED':
            return False

        # Check the current and desired positions to ensure they are both on the board (in the board dictionary)
        if start_pos not in self._board or end_pos not in self._board:
            return False

        # Check that there is some piece at the start position
        if self._board[start_pos] is None:
            return False

        # Check that the piece at the starting position is the same color as the turn data member
        if self._board[start_pos].get_color() != self._turn:
            return False

        # Check that the piece at the desired position is empty or does not have the same color as the turn data member
        try:
            end_pos_piece_color = self._board[end_pos].get_color()
        except AttributeError:  # AttributeError occurs when the end_pos None (empty). This does not prevent movement
            pass
        else:
            # if the get color method does not cause an error than there is a piece at end position, check its color
            if end_pos_piece_color == self._turn:
                return False

        # If False has not yet been returned then call a move method for a specific piece
        # (like move_castle or move_pawn), passing the current and desired position as parameters.
        start_pos_piece_type = self._board[start_pos].get_kind()
        # The specific move method will return True if the move was completed and False if move was not possible
        if start_pos_piece_type == 'Pawn':
            return self.move_pawn(start_pos, end_pos)
        if start_pos_piece_type == 'Castle':
            return self.move_castle(start_pos, end_pos)
        if start_pos_piece_type == 'Knight':
            return self.move_knight(start_pos, end_pos)
        if start_pos_piece_type == 'Bishop':
            return self.move_bishop(start_pos, end_pos)
        if start_pos_piece_type == 'Queen':
            return self.move_queen(start_pos, end_pos)
        else:  # Only King remains, if not above then we are moving the King piece
            return self.move_king(start_pos, end_pos)

    def move_pawn(self, start_pos, end_pos):
        """
        Attempts to update the current position of the pawn from the start position to the end position.
        Creates a list of possible move positions based on the piece and the current board state. If the end position is
        in the list of possible positions then the pawn's position is updated and True is returned. If the end position
        is not possible then the pawn's position is not updated and False is returned.
        An end position may still be impossible because:
        1. The piece is incapable of moving that far or in that direction/pattern
        2. A piece is blocking the way
        :param start_pos: A string representing the current position of the pawn to be moved (like 'a7')
        :param end_pos: A string representing the desired position of the pawn to be moved (like 'a6')
        :return: True if move completed, False if not completed due to it being invalid
        """
        possible_pos = []
        pawn_color = self._board[start_pos].get_color()

        # Add all possible moves forward
        if pawn_color == 'White':  # we must treat white and black pieces differently for pawns

            # if the pawn is in the starting position (first row), then it can move 2 spaces
            if int(start_pos[1]) == 2:
                if self._board[start_pos[0] + '3'] is None:  # Check that space is not blocked
                    if self._board[start_pos[0] + '4'] is None:  # Checks space is empty, pawns only attack diagonal
                        possible_pos.append(start_pos[0] + '4')

            # no matter where the pawn is, it can move forward if there is another empty space
            if start_pos[0] + str(int(start_pos[1]) + 1) in self._board:
                if self._board[start_pos[0] + str(int(start_pos[1]) + 1)] is None:
                    possible_pos.append(start_pos[0] + str(int(start_pos[1]) + 1))

            # if an opposing player's piece is forward/LEFT diagonal of pawn then it may attack it
            # new position finds forward/left diagonal unless forward left diagonal is off board
            # then changes letter to z
            new_position = number_to_letter(letter_to_number(start_pos[0]) - 1) + str(int(start_pos[1]) + 1)
            if new_position in self._board:
                if self._board[new_position] is not None:  # can only move diagonal when attacking enemy piece
                    if self._board[new_position].get_color() != self._turn:
                        possible_pos.append(new_position)

            # repeat steps for if an opposing player's piece is forward/RIGHT diagonal of pawn then it may attack it
            # we overwrite the new_position variable to new space we are considering
            new_position = number_to_letter(letter_to_number(start_pos[0]) + 1) + str(int(start_pos[1]) + 1)
            if new_position in self._board:
                if self._board[new_position] is not None:  # can only move diagonal when attacking enemy piece
                    if self._board[new_position].get_color() != self._turn:
                        possible_pos.append(new_position)

        # Now we have added all moves if the piece is white, we need to repeat for black
        if pawn_color == 'Black':

            # if the pawn is in the starting position (first row), then it can move 2 spaces
            if int(start_pos[1]) == 7:
                if self._board[start_pos[0] + '6'] is None:  # Check that space is not blocked
                    if self._board[start_pos[0] + '5'] is None:  # Checks space is empty, pawns can't attack straight
                        possible_pos.append(start_pos[0] + '5')

            # no matter where the pawn is, it can move forward if there is another empty space
            if start_pos[0] + str(int(start_pos[1]) - 1) in self._board:
                if self._board[start_pos[0] + str(int(start_pos[1]) - 1)] is None:
                    possible_pos.append(start_pos[0] + str(int(start_pos[1]) - 1))

            # if an opposing player's piece is forward/LEFT diagonal of pawn then it may attack it
            # new position finds forward/left diagonal unless forward left diagonal is off board
            # then changes letter to z
            new_position = number_to_letter(letter_to_number(start_pos[0]) - 1) + str(int(start_pos[1]) - 1)
            if new_position in self._board:
                if self._board[new_position] is not None:  # can only move diagonal when attacking enemy piece
                    if self._board[new_position].get_color() != self._turn:
                        possible_pos.append(new_position)

            # repeat steps for if an opposing player's piece is forward/RIGHT diagonal of pawn then it may attack it
            # we overwrite the new_position variable to new space we are considering
            new_position = number_to_letter(letter_to_number(start_pos[0]) + 1) + str(int(start_pos[1]) - 1)
            if new_position in self._board:
                if self._board[new_position] is not None:  # can only move diagonal when attacking enemy piece
                    if self._board[new_position].get_color() != self._turn:
                        possible_pos.append(new_position)

        # Check if the position we are moving to is possible, return False if impossible
        if end_pos not in possible_pos:
            return False

        # Check if we are capturing a piece
        if self._board[end_pos] is not None:
            # if there is a piece there then we are capturing the piece as we move to the space
            self.capture_piece(end_pos)
            self._board[end_pos] = self._board[start_pos]  # end position now has the piece at start position
            self._board[start_pos] = None  # and the start position is empty
            self.next_turn()
            return True

        # If not capturing, we are moving onto a blank space
        else:
            self._board[end_pos] = self._board[start_pos]  # end position now has the piece at start position
            self._board[start_pos] = None  # and the start position is empty
            self.next_turn()
            return True

    def move_castle(self, start_pos, end_pos):
        """
        Attempts to update the current position of the castle from the start position to the end position.
        Creates a list of possible move positions based on the piece and the current board state. If the end position is
        in the list of possible positions, the castle's position is updated and True is returned. If the end position
        is not possible then the castle's position is not updated and False is returned.
        An end position may still be impossible because:
        1. The piece is incapable of moving that in that direction/pattern
        2. A piece is blocking the way
        :param start_pos: A string representing the current position of the castle to be moved (like 'a7')
        :param end_pos: A string representing the desired position of the castle to be moved (like 'a6')
        :return: True if move completed, False if not completed due to it being invalid
        """
        possible_pos = []
        castle_color = self._board[start_pos].get_color()

        # While we used terms like backward and forward, these are correct if White but reversed if the piece is Black
        # Add all possible moves forward to list of possible moves
        next_space = start_pos[0] + str(int(start_pos[1]) + 1)
        # first we add all the empty forward spaces to possible moves
        while next_space in self._board and self._board[next_space] is None:
            possible_pos.append(next_space)
            next_space = next_space[0] + str(int(next_space[1]) + 1)

        # Once all empty spaces added, next_space has a piece or is off the board
        if next_space in self._board:
            # Check if the piece is an opposing color and can be captured
            if self._board[next_space].get_color() != castle_color:
                possible_pos.append(next_space)

        # Add all possible moves backward to list of possible moves
        next_space = start_pos[0] + str(int(start_pos[1]) - 1)
        # first we add all the empty backward spaces to possible moves
        while next_space in self._board and self._board[next_space] is None:
            possible_pos.append(next_space)
            next_space = next_space[0] + str(int(next_space[1]) - 1)

        # Once all empty spaces added, next_space has a piece or is off the board
        if next_space in self._board:
            # Check if the piece is an opposing color and can be captured
            if self._board[next_space].get_color() != castle_color:
                possible_pos.append(next_space)

        # Add all possible moves rightward to list of possible moves
        next_space = number_to_letter(letter_to_number(start_pos[0]) + 1) + start_pos[1]
        # first we add all the empty rightward spaces to possible moves
        while next_space in self._board and self._board[next_space] is None:
            possible_pos.append(next_space)
            next_space = number_to_letter(letter_to_number(next_space[0]) + 1) + next_space[1]

        # Once all empty spaces added, next_space has a piece or is off the board
        if next_space in self._board:
            # Check if the piece is an opposing color and can be captured
            if self._board[next_space].get_color() != castle_color:
                possible_pos.append(next_space)

        # Add all possible moves leftward to list of possible moves
        next_space = number_to_letter(letter_to_number(start_pos[0]) - 1) + start_pos[1]
        # first we add all the empty leftward spaces to possible moves
        while next_space in self._board and self._board[next_space] is None:
            possible_pos.append(next_space)
            next_space = number_to_letter(letter_to_number(next_space[0]) - 1) + next_space[1]

        # Once all empty spaces added, next_space has a piece or is off the board
        if next_space in self._board:
            # Check if the piece is an opposing color and can be captured
            if self._board[next_space].get_color() != castle_color:
                possible_pos.append(next_space)

        # Check if the position we are moving to is possible, return False if impossible
        if end_pos not in possible_pos:
            return False

        # Check if we are capturing a piece
        if self._board[end_pos] is not None:
            # if there is a piece there then we are capturing the piece as we move to the space
            self.capture_piece(end_pos)
            self._board[end_pos] = self._board[start_pos]  # end position now has the piece at start position
            self._board[start_pos] = None  # and the start position is empty
            self.next_turn()
            return True

        # If not capturing, we are moving onto a blank space
        else:
            self._board[end_pos] = self._board[start_pos]  # end position now has the piece at start position
            self._board[start_pos] = None  # and the start position is empty
            self.next_turn()
            return True

    def move_knight(self, start_pos, end_pos):
        """
        Attempts to update the current position of the knight from the start position to the end position.
        Creates a list of possible move positions based on the piece and the current board state. If the end position is
        in the list of possible positions then the knight's position is updated and True is returned.
        If the end position is not possible then the knight's position is not updated and False is returned.
        An end position may still be impossible because:
        1. The piece is incapable of moving that far or in that direction/pattern
        :param start_pos: A string representing the current position of the knight to be moved (like 'a7')
        :param end_pos: A string representing the desired position of the knight to be moved (like 'a6')
        :return: True if move completed, False if not completed due to it being invalid
        """
        possible_pos = []
        knight_color = self._board[start_pos].get_color()

        # While we used terms like backward and forward, these are correct if White but reversed if the piece is Black
        # Add all possible knight moves to list of possible moves
        # At most, a knight has 8 moves
        forward_left = number_to_letter(letter_to_number(start_pos[0]) - 1) + str(int(start_pos[1]) + 2)
        forward_right = number_to_letter(letter_to_number(start_pos[0]) + 1) + str(int(start_pos[1]) + 2)
        right_forward = number_to_letter(letter_to_number(start_pos[0]) + 2) + str(int(start_pos[1]) + 1)
        right_backward = number_to_letter(letter_to_number(start_pos[0]) + 2) + str(int(start_pos[1]) - 1)
        backward_left = number_to_letter(letter_to_number(start_pos[0]) - 1) + str(int(start_pos[1]) - 2)
        backward_right = number_to_letter(letter_to_number(start_pos[0]) + 1) + str(int(start_pos[1]) - 2)
        left_forward = number_to_letter(letter_to_number(start_pos[0]) - 2) + str(int(start_pos[1]) + 1)
        left_backward = number_to_letter(letter_to_number(start_pos[0]) - 2) + str(int(start_pos[1]) - 1)

        spaces = [forward_left, forward_right, right_forward, right_backward, backward_left, backward_right,
                  left_forward, left_backward]

        # Check which of the 8 spaces are possible and add them to possible moves
        for space in spaces:
            if space in self._board:
                if self._board[space] is None or self._board[space].get_color() != knight_color:
                    possible_pos.append(space)

        # Check if the position we are moving to is possible, return False if impossible
        if end_pos not in possible_pos:
            return False

        # Check if we are capturing a piece
        if self._board[end_pos] is not None:
            # if there is a piece there then we are capturing the piece as we move to the space
            self.capture_piece(end_pos)
            self._board[end_pos] = self._board[start_pos]  # end position now has the piece at start position
            self._board[start_pos] = None  # and the start position is empty
            self.next_turn()
            return True

        # If not capturing, we are moving onto a blank space
        else:
            self._board[end_pos] = self._board[start_pos]  # end position now has the piece at start position
            self._board[start_pos] = None  # and the start position is empty
            self.next_turn()
            return True

    def move_bishop(self, start_pos, end_pos):
        """
        Attempts to update the current position of the bishop from the start position to the end position.
        Creates a list of possible move positions based on the piece and the current board state. If the end position is
        in the list of possible positions then the bishop's position is updated and True is returned.
        If the end position is not possible then the bishop's position is not updated and False is returned.
        An end position may still be impossible because:
        1. The piece is incapable of moving that far or in that direction/pattern
        2. A piece is blocking the way
        :param start_pos: A string representing the current position of the bishop to be moved (like 'a7')
        :param end_pos: A string representing the desired position of the bishop to be moved (like 'a6')
        :return: True if move completed, False if not completed due to it being invalid
        """
        possible_pos = []
        bishop_color = self._board[start_pos].get_color()

        # While we used terms like backward and forward, these are correct if White but reversed if the piece is Black
        # Add all possible moves for forward/left diagonal to list of possible moves
        next_space = number_to_letter(letter_to_number(start_pos[0]) - 1) + str(int(start_pos[1]) + 1)
        # first we add all the empty forward/left spaces to possible moves
        while next_space in self._board and self._board[next_space] is None:
            possible_pos.append(next_space)
            next_space = number_to_letter(letter_to_number(next_space[0]) - 1) + str(int(next_space[1]) + 1)

        # Once all empty spaces added, next_space has a piece or is off the board
        if next_space in self._board:
            # Check if the piece is an opposing color and can be captured
            if self._board[next_space].get_color() != bishop_color:
                possible_pos.append(next_space)

        # Add all possible moves for forward/right diagonal to list of possible moves
        # We overwrite next space to point to next forward/right diagonal space
        next_space = number_to_letter(letter_to_number(start_pos[0]) + 1) + str(int(start_pos[1]) + 1)
        # first we add all the empty forward/right spaces to possible moves
        while next_space in self._board and self._board[next_space] is None:
            possible_pos.append(next_space)
            next_space = number_to_letter(letter_to_number(next_space[0]) + 1) + str(int(next_space[1]) + 1)

        # Once all empty spaces added, next_space has a piece or is off the board
        if next_space in self._board:
            # Check if the piece is an opposing color and can be captured
            if self._board[next_space].get_color() != bishop_color:
                possible_pos.append(next_space)

        # Add all possible moves for backward/right diagonal to list of possible moves
        # We overwrite next space to point to next backward/right diagonal space
        next_space = number_to_letter(letter_to_number(start_pos[0]) + 1) + str(int(start_pos[1]) - 1)
        # first we add all the empty backward/right spaces to possible moves
        while next_space in self._board and self._board[next_space] is None:
            possible_pos.append(next_space)
            next_space = number_to_letter(letter_to_number(next_space[0]) + 1) + str(int(next_space[1]) - 1)

        # Once all empty spaces added, next_space has a piece or is off the board
        if next_space in self._board:
            # Check if the piece is an opposing color and can be captured
            if self._board[next_space].get_color() != bishop_color:
                possible_pos.append(next_space)

        # Add all possible moves for backward/left diagonal to list of possible moves
        # We overwrite next space to point to next backward/left diagonal space
        next_space = number_to_letter(letter_to_number(start_pos[0]) - 1) + str(int(start_pos[1]) - 1)
        # first we add all the empty backward/left spaces to possible moves
        while next_space in self._board and self._board[next_space] is None:
            possible_pos.append(next_space)
            next_space = number_to_letter(letter_to_number(next_space[0]) - 1) + str(int(next_space[1]) - 1)

        # Once all empty spaces added, next_space has a piece or is off the board
        if next_space in self._board:
            # Check if the piece is an opposing color and can be captured
            if self._board[next_space].get_color() != bishop_color:
                possible_pos.append(next_space)

        # Check if the position we are moving to is possible, return False if impossible
        if end_pos not in possible_pos:
            return False

        # Check if we are capturing a piece
        if self._board[end_pos] is not None:
            # if there is a piece there then we are capturing the piece as we move to the space
            self.capture_piece(end_pos)
            self._board[end_pos] = self._board[start_pos]  # end position now has the piece at start position
            self._board[start_pos] = None  # and the start position is empty
            self.next_turn()
            return True

        # If not capturing, we are moving onto a blank space
        else:
            self._board[end_pos] = self._board[start_pos]  # end position now has the piece at start position
            self._board[start_pos] = None  # and the start position is empty
            self.next_turn()
            return True

    def move_queen(self, start_pos, end_pos):
        """
        Attempts to update the current position of the queen from the start position to the end position.
        Creates a list of possible move positions based on the piece and the current board state. If the end position is
        in the list of possible positions then the queen's position is updated and True is returned.
        If the end position is not possible then the queen's position is not updated and False is returned.
        An end position may still be impossible because:
        1. The piece is incapable of moving that far or in that direction/pattern
        2. A piece is blocking the way
        :param start_pos: A string representing the current position of the queen to be moved (like 'a7')
        :param end_pos: A string representing the desired position of the queen to be moved (like 'a6')
        :return: True if move completed, False if not completed due to it being invalid
        """
        # A Queen can move like a Castle or a Bishop so we cna reuse other move methods
        # If the Queen ends up in the same row column from where it started then it is moving like a Castle
        if start_pos[0] == end_pos[0] or start_pos[1] == end_pos[1]:
            return self.move_castle(start_pos, end_pos)
        # Otherwise the Queen is moving like a Bishop
        else:
            return self.move_bishop(start_pos, end_pos)

    def move_king(self, start_pos, end_pos):
        """
        Attempts to update the current position of the king from the start position to the end position.
        Creates a list of possible move positions based on the piece and the current board state. If the end position is
        in the list of possible positions then the king's position is updated and True is returned.
        If the end position is not possible then the king's position is not updated and False is returned.
        An end position may still be impossible because:
        1. The piece is incapable of moving that far
        2. A piece is blocking the way
        :param start_pos: A string representing the current position of the king to be moved (like 'a7')
        :param end_pos: A string representing the desired position of the king to be moved (like 'a6')
        :return: True if move completed, False if not completed due to it being invalid
        """
        possible_pos = []
        king_color = self._board[start_pos].get_color()

        # While we used terms like backward and forward, these are correct if White but reversed if the piece is Black
        # Add all possible king moves to list of possible moves
        # At most, a king has 8 moves
        forward_left = number_to_letter(letter_to_number(start_pos[0]) - 1) + str(int(start_pos[1]) + 1)
        forward = start_pos[0] + str(int(start_pos[1]) + 1)
        forward_right = number_to_letter(letter_to_number(start_pos[0]) + 1) + str(int(start_pos[1]) + 1)
        right = number_to_letter(letter_to_number(start_pos[0]) + 1) + start_pos[1]
        backward_right = number_to_letter(letter_to_number(start_pos[0]) + 1) + str(int(start_pos[1]) - 1)
        backward = start_pos[0] + str(int(start_pos[1]) - 1)
        backward_left = number_to_letter(letter_to_number(start_pos[0]) - 1) + str(int(start_pos[1]) - 1)
        left = number_to_letter(letter_to_number(start_pos[0]) - 1) + start_pos[1]

        spaces = [forward_left, forward, forward_right, right, backward_right, backward, backward_left, left]

        # Check which of the 8 spaces are possible and add them to possible moves
        for space in spaces:
            if space in self._board:
                if self._board[space] is None or self._board[space].get_color() != king_color:
                    possible_pos.append(space)

        # Check if the position we are moving to is possible, return False if impossible
        if end_pos not in possible_pos:
            return False

        # Check if we are capturing a piece
        if self._board[end_pos] is not None:
            # if there is a piece there then we are capturing the piece as we move to the space
            self.capture_piece(end_pos)
            self._board[end_pos] = self._board[start_pos]  # end position now has the piece at start position
            self._board[start_pos] = None  # and the start position is empty
            self.next_turn()
            return True

        # If not capturing, we are moving onto a blank space
        else:
            self._board[end_pos] = self._board[start_pos]  # end position now has the piece at start position
            self._board[start_pos] = None  # and the start position is empty
            self.next_turn()
            return True
