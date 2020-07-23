# Author: Leon Samuel
# Date: March 04, 2020
# Description: Computer program version of Xiangqi Game using python objects


class XiangqiGame:
    """
    creates object for the Xiangqi Game
    """

    def __init__(self):
        """Creates an object for a Xiangqi Game using objects to represent the board and pieces."""
        self._board = Board()
        self._pieces = Pieces()
        self._player_turn = "red"
        self._game_state = 'UNFINISHED'
        self._is_in_check = None
        self._all_pieces = []

        """initialize each piece using subclass, team color, name of peice, and position on board"""
        p1 = Pawn("red", "pawn", "P", 0, 3)
        p2 = Pawn("red", "pawn", "P", 2, 3)
        p3 = Pawn("red", "pawn", "P", 4, 3)
        p4 = Pawn("red", "pawn", "P", 6, 3)
        p5 = Pawn("red", "pawn", "P", 8, 3)
        p6 = Pawn("black", "pawn", "P", 0, 6)
        p7 = Pawn("black", "pawn", "P", 2, 6)
        p8 = Pawn("black", "pawn", "P", 4, 6)
        p9 = Pawn("black", "pawn", "P", 6, 6)
        p10 = Pawn("black", "pawn", "P", 8, 6)
        k1 = Knight("red", "knight", "K", 1, 0)
        k2 = Knight("red", "knight", "K", 7, 0)
        k3 = Knight("black", "knight", "K", 1, 9)
        k4 = Knight("black", "knight", "K", 7, 9)
        e1 = Elephant("red", "elephant", "E", 2, 0)
        e2 = Elephant("red", "elephant", "E", 6, 0)
        e3 = Elephant("black", "elephant", "E", 2, 9)
        e4 = Elephant("black", "elephant", "E", 6, 9)
        rook1 = Rook("red", "rook", "R", 0, 0)
        rook2 = Rook("red", "rook", "R", 8, 0)
        rook3 = Rook("black", "rook", "R", 0, 9)
        rook4 = Rook("black", "rook", "R", 8, 9)
        cannon1 = Cannon("red", "cannon", "C", 1, 2)
        cannon2 = Cannon("red", "cannon", "C", 7, 2)
        cannon3 = Cannon("black", "cannon", "C", 1, 7)
        cannon4 = Cannon("black", "cannon", "C", 7, 7)
        a1 = Advisor("red", "advisor", "A", 3, 0)
        a2 = Advisor("red", "advisor", "A", 5, 0)
        a3 = Advisor("black", "advisor", "A", 3, 9)
        a4 = Advisor("black", "advisor", "A", 5, 9)
        g1 = General("red", "general", "G", 5, 0)
        g2 = General("black", "general", "G", 5, 9)

        """make pieces easily accessible, probably a better way to do this"""
        self.add_piece(p1)
        self.add_piece(p2)
        self.add_piece(p3)
        self.add_piece(p4)
        self.add_piece(p5)
        self.add_piece(p6)
        self.add_piece(p7)
        self.add_piece(p8)
        self.add_piece(p9)
        self.add_piece(p10)
        self.add_piece(k1)
        self.add_piece(k2)
        self.add_piece(k3)
        self.add_piece(k4)
        self.add_piece(e1)
        self.add_piece(e2)
        self.add_piece(e3)
        self.add_piece(e4)
        self.add_piece(rook1)
        self.add_piece(rook2)
        self.add_piece(rook3)
        self.add_piece(rook4)
        self.add_piece(cannon1)
        self.add_piece(cannon2)
        self.add_piece(cannon3)
        self.add_piece(cannon4)
        self.add_piece(a1)
        self.add_piece(a2)
        self.add_piece(a3)
        self.add_piece(a4)
        self.add_piece(g1)
        self.add_piece(g2)


    def add_piece(self, piece):
        """ adds the item to holdings """
        self._all_pieces.append(piece)

    def get_legal_moves(self):
        """populates legal moves in class before first move - testing needed"""
        for i in self._all_pieces:
            i.get_legal_moves()

    def convert_coordinates(self, position):
        """converts player passed coordinates so that they work with list set up of game"""
        char_to_num = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            "i": 8
        }

        column = char_to_num[position[:1]]
        row = int(position[1:]) - 1
        return column, row

    def get_player_turn(self):
        """returns current player turn"""
        return self._player_turn

    def set_player_turn(self, color):
        """changes next player"""
        self._player_turn = color

    def make_move(self, start, end):
        """Performs initial testing of potential move before passing to specific piece move method"""
        start_col, start_row = self.convert_coordinates(start)
        end_col, end_row = self.convert_coordinates(end)
        self._board.get_board()
        board = self._board.get_board()
        label = board[start_row][start_col]
        if self._game_state == 'UNFINISHED':
            for i in self._all_pieces:
                if i.get_board_label() == label and i.get_color() == self._player_turn and i.get_start_col() == start_col and i.get_start_row() == start_row and i.get_captured() is False:
                    return i.make_move(self._board, self, start_col, start_row, end_col, end_row)

        return False

    def get_all_pieces(self):
        """returns all pieces"""
        return self._all_pieces

    def get_game_state(self):
        """Returns game state - unfinsihed or won"""
        return self._game_state

    def is_in_check(self, color):
        """Returns True or False based on if passed team color is in check"""
        if self._is_in_check == color:
            return True
        return False

    def set_is_in_check(self, color):
        """Changes the check state of game based on passed team color"""
        self._is_in_check = color

    def set_game_state(self, general):
        """Changes game state to reflect winner based on not being able to escape check"""
        if self._is_in_check is not None:
            if general.get_color == "red":
                general.set_legal_moves()
                if general.get_legal_moves() == []:
                    self._game_state = 'BLACK_WON'
            if general.get_color == "black":
                general.set_legal_moves()
                if general.get_legal_moves() == []:
                    self._game_state = 'RED_WON'

    def set_game_state_stalemate(self):
        """Changes game state if team is not in check but do not having legal moves remaining """
        red_legal_moves = []
        black_legal_moves = []

        for i in self._all_pieces:
            if i.get_color() == "red" and i.get_captured() is False:
                for r in i.get_legal_moves():
                    red_legal_moves.append(r)

        if red_legal_moves == []:
            self._game_state = 'BLACK_WON'

        for i in self._all_pieces:
            if i.get_color() == "black" and i.get_captured() is False:
                for r in i.get_legal_moves():
                    black_legal_moves.append(r)

        if black_legal_moves == []:
            self._game_state = 'BLACK_WON'

    def set_general_check(self, color):
        """Changes check state of game based on if any general is in check at end of turn - accounts for double check"""
        if color == "black":
            for i in self._all_pieces: #starts to find red general
                if i.get_board_label == "G" and i.get_color == "red":
                    red_general = i
                    for r in self._all_pieces: #if red general coords is in legal moves then changes in-check to red
                        if red_general.get_coords in r.get_legal_moves:
                            self.set_is_in_check("red")

            for i in self._all_pieces: #does same step with black since if black peice puts same team in check then move has to be reversed, doing it secondary accounts for siutations where both generals would be in check but would have to be undone since this peice causes own team to be in check
                if i.get_board_label == "G" and i.get_color == "black":
                    black_general = i
                    for r in self._all_pieces:
                        if black_general.get_coords in r.get_legal_moves:
                            self.set_is_in_check("black")

            for i in self._all_pieces:
                if i.get_board_label == "G" and i.get_color == "black":
                    black_general = i
                    for r in self._all_pieces:  # finds red general
                        if r.get_board_label == "G" and i.get_color == "red":
                            red_general = r
                            if black_general.get_coords not in i.get_legal_moves and red_general.get_coords not in i.get_legal_moves:
                                self.set_is_in_check(None)
            return

        if color == "red":
            for i in self._all_pieces:
                if i.get_board_label == "G" and i.get_color == "black":
                    black_general = i
                    for r in self._all_pieces:
                        if black_general.get_coords in r.get_legal_moves:
                            self.set_is_in_check("black")

            for i in self._all_pieces:
                if i.get_board_label == "G" and i.get_color == "red":
                    red_general = i
                    for r in self._all_pieces:
                        if red_general.get_coords in r.get_legal_moves:
                            self.set_is_in_check("red")

            for i in self._all_pieces:
                if i.get_board_label == "G" and i.get_color == "black":
                    black_general = i
                    for r in self._all_pieces:  # finds red general
                        if r.get_board_label == "G" and i.get_color == "red":
                            red_general = r
                            if black_general.get_coords not in i.get_legal_moves and red_general.get_coords not in i.get_legal_moves:
                                self.set_is_in_check(None)
            return

    def all_pieces(self):
        """returns all pieces - duplicate but need to search to see if used elsewhere"""
        return self._all_pieces


class Board:
    """Creates an object for a Xiangqi board"""
    def __init__(self):
        """ Creates and maintains board for game """
        self._board = \
        [["R","K", "E", "A", "G", "A", "E", "K", "R"],
        ["", "", "", "", "", "", "", "", ""],
        ["", "C", "", "", "", "", "", "C", ""],
        ["P", "", " P", "", "P", "", "P", "", "P"],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["P", "", " P", "", "P", "", "P", "", "P"],
        ["", "C", "", "", "", "", "", "C", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["R", "K", "E", "A", "G", "A", "E", "K", "R"]]

    def get_board(self):
        """Returns board"""
        return self._board

    def get_label_from_board(self, start_col, start_row):
        """Returns label at board to ensure right location is selected for move"""
        return self._board[start_col][start_row]

    def print_board(self):
        """Prints board in loose board format"""
        for line in self._board:
            print(line)
        print()

    def update_board(self, start_col, start_row, end_col, end_row, label):
        """updates board based on move"""
        self._board[start_row][start_col] = ""
        self._board[end_row][end_col] = label
        self.print_board()

class Pieces:
    """
    Contains rules pertaining to all pieces
    """

    def __init__(self):
        self.holder = None


class Regiment(Pieces):
    """Handles super information and method for piece classes"""
    def __init__(self, team_color, name, board_label, start_col, start_row):
        """ creates and maintains board for game """
        self._color = team_color
        self._name = name
        self._board_label = board_label
        self._start_col = start_col
        self._start_row = start_row
        self._captured = False
        super().__init__()

    def get_is_in_bounds(self, end_col, end_row):
        """returns True or False if in bounds of game board"""
        return 0 <= end_col <= 8 and 0 <= end_row >= 8

    def get_color(self):
        """Returns pieces color"""
        return self._color

    def get_start_col(self):
        """Returns starting column of peice"""
        return self._start_col

    def get_start_row(self):
        """Returns starting row of piece"""
        return self._start_row

    def get_coords(self):
        """Returns coordinates of piece of board"""
        return [self._start_col, self._start_row]

    def get_board_label(self):
        """Returns board label for game board"""
        return self._board_label

    def set_captured(self):
        """Sets piece captured to true if captured"""
        self._captured = True

    def get_captured(self):
        """Returns capture data memeber"""
        return self._captured

    def set_uncapture(self):
        """Sets captured status to False if move is undone"""
        self._captured = False

    def set_moved(self, end_col, end_row):
        """changing current data memebers to new location since legal move was performed"""
        self._start_col = end_col
        self._start_row = end_row

    def set_all_next_steps(self, game):
        """Calculates next legal moves for all pieces"""
        for i in game.get_all_pieces():
            if i.get_captured() is False:
                i.set_legal_moves(game)


    def get_red_general(self, game):
        """Returns red general"""
        for i in game.get_all_pieces():
            if i.get_board_label == "G" and i.get_color == "red":
                return i

    def get_black_general(self, game):
        """Returns black general"""
        for i in game.get_all_pieces():
            if i.get_board_label == "G" and i.get_color == "black":
                return i

    def flying_general_check(self, red_general, black_general, game):
        """Ensures generals will not see each other"""
        if black_general.get_start_col() ==  red_general.get_start_col():
            for i in game.get_all_pieces:
                if i.get_start_col() == black_general.get_start_col():
                    return True

    def get_legal_moves(self):
        return self._legal_moves

    def make_move(self, board, game, start_col, start_row, end_col, end_row):
        """tests for moves legality and changes all objects accordingly, as well as undoing illegal moves"""
        self.set_legal_moves(game)
        if [end_col, end_row] in self._legal_moves:
            for i in game.get_all_pieces():
                if i.get_coords == [end_col, end_row]:
                    if i.get_color == self._color:
                        return False #same color piece is at that location
                    if i.get_color != self._color: #if opposing team piece here, then capture it
                        i.set_captured()
            self.set_moved(end_col, end_row) #move piece to location
            self.set_all_next_steps(game) #update next steps to see if general will be in check
            game.set_general_check(self._color)
            if game.is_in_check(self._color) is True:
                self.set_moved(start_col, start_row)
                self.get_legal_moves()  #undo populated moves since move leaves same team general in check
                for i in game.get_all_pieces():
                    if i.get_coords == [end_col, end_row]:
                        if i.get_color != self._color:
                            i.set_uncapture()
                return False
            board.update_board(start_col, start_row, end_col, end_row, self._board_label)
            if self.get_color == "black" and game.is_in_check("red") is True:
                red_general = game.get_red_general(self, game)
                game.set_game_state(self, red_general)
            if self.get_color == "red" and game.is_in_check("black") is True:
                black_general = game.get_black_general(self, game)
                game.set_game_state(self, black_general)
            game.set_game_state_stalemate()
            if game.get_player_turn() == "red":
                game._player_turn = "black"
                return True
            if game.get_player_turn() == "black":
                game._player_turn = "red"
                return True

class Pawn(Regiment):
    """
    Child of Pieces class, contains special rules pertaining to the piece
    """

    def __init__(self, team_color, name, board_label, start_col, start_row):
        """ creates object for a movie based on stated parameters """
        super().__init__(team_color, name, board_label, start_col, start_row)
        self._legal_moves = [] #holds list of pairings of possible moves where teammates are not located

    def make_move(self, board, game, start_col, start_row, end_col, end_row):
        """passes move to parent object for testing"""
        return super().make_move(board, game, start_col, start_row, end_col, end_row)

    def set_legal_moves(self, game):
        """clear and creates a list of possible moves for the object"""
        del self._legal_moves[:]

        if self._color == "red":
            if self._start_row < 5: #can only move forward
                self._legal_moves.append([self._start_col, self._start_row + 1])
            if self._start_row >= 5:
                if self._start_col - 1 < 0 and self._start_row + 1 > 9: #top left corner, can only move right
                    self._legal_moves.append([self._start_col + 1, self._start_row])
                if self._start_col + 1 < 8 and self._start_row + 1 > 9: #top right corner, can only move left
                    self._legal_moves.append([self._start_col - 1, self._start_row])
                if 1 >= self._start_col < 7 and self._start_row == 9:  # top but not in corner
                    self._legal_moves.append([self._start_col - 1, self._start_row])
                    self._legal_moves.append([self._start_col + 1, self._start_row])
                if self._start_col == 0: #not at top, but on left edge of board
                    self._legal_moves.append([self._start_col, self._start_row + 1])
                    self._legal_moves.append([self._start_col + 1, self._start_row])
                if self._start_col == 8: #not at top, but on right edge of board
                    self._legal_moves.append([self._start_col, self._start_row + 1])
                    self._legal_moves.append([self._start_col - 1, self._start_row])
                if self._start_col != 0 and self._start_col != 8 and self._start_row != 9: #not at top and not on an edge middle
                    self._legal_moves.append([self._start_col, self._start_row + 1])
                    self._legal_moves.append([self._start_col + 1, self._start_row])
                    self._legal_moves.append([self._start_col - 1, self._start_row])
                return

        if self._color == "black":
            if self._start_row > 5: #can only move forward
                #print("got here black")
                self._legal_moves.append([self._start_col, self._start_row - 1])
            if self._start_row <= 5:
                #print("got here too red")
                if self._start_col == 0 and self._start_row == 0: #bottom left corner, can only move right
                    self._legal_moves.append([self._start_col + 1, self._start_row])
                if self._start_col == 8 and self._start_row == 0: #bottom right corner, can only move left
                    self._legal_moves.append([self._start_col - 1, self._start_row])
                if 1 >= self._start_col < 7 and self._start_row == 0:  # bottom but not in corner
                    self._legal_moves.append([self._start_col - 1, self._start_row])
                    self._legal_moves.append([self._start_col + 1, self._start_row])
                if self._start_col == 0: #not at bottom, but on left edge of board
                    self._legal_moves.append([self._start_col, self._start_row - 1])
                    self._legal_moves.append([self._start_col + 1, self._start_row])
                if self._start_col == 8: #not at bottom, but on right edge of board
                    self._legal_moves.append([self._start_col, self._start_row - 1])
                    self._legal_moves.append([self._start_col - 1, self._start_row])
                if self._start_col != 0 and self._start_col != 8 and self._start_row != 0: #not at bottom and not on an edge middle
                    self._legal_moves.append([self._start_col, self._start_row - 1])
                    self._legal_moves.append([self._start_col + 1, self._start_row])
                    self._legal_moves.append([self._start_col - 1, self._start_row])
                return

            for i in game.get_all_pieces():
                if self.get_color == i.get_color:
                    if i.get_coords in self._legal_moves:
                        self._legal_moves.remove(i.get_coords)

class Knight(Regiment):
    """
    Child of Pieces class, contains special rules pertaining to the piece
    """

    def __init__(self, team_color, name, board_label, start_col, start_row):
        """ creates object for a movie based on stated parameters """
        super().__init__(team_color, name, board_label, start_col, start_row)
        self._legal_moves = []

    def make_move(self, board, game, start_col, start_row, end_col, end_row):
        """passes move to parent object for testing"""
        return super().make_move(board, game, start_col, start_row, end_col, end_row)

    def set_legal_moves(self, game):
        """clear and creates a list of possible moves for the object"""
        del self._legal_moves[:]

        self._legal_moves.append([self._start_col + 1, self._start_row + 2])
        self._legal_moves.append([self._start_col - 1, self._start_row + 1])
        self._legal_moves.append([self._start_col + 1, self._start_row - 1])
        self._legal_moves.append([self._start_col - 2, self._start_row + 1])
        self._legal_moves.append([self._start_col + 2, self._start_row + 1])
        self._legal_moves.append([self._start_col - 2, self._start_row - 1])
        self._legal_moves.append([self._start_col + 2, self._start_row - 1])
        self._legal_moves.append([self._start_col - 1, self._start_row + 2])


        for coords in self._legal_moves:
            for col in coords[:1]:
                if col > 9 or col < 0:
                    self._legal_moves.remove(coords)

        for coords in self._legal_moves:
            for row in coords[1:]:
                if row > 10 or row <= 0:
                    self._legal_moves.remove(coords)


        for i in game.get_all_pieces():
            if self.get_color == i.get_color:
                if i.get_coords in self._legal_moves:
                    self._legal_moves.remove(i.get_coords)

class Elephant(Regiment):
    """
    Child of Pieces class, contains special rules pertaining to the piece
    """

    def __init__(self, team_color, name, board_label, start_col, start_row):
        """ creates object for a movie based on stated parameters """
        super().__init__(team_color, name, board_label, start_col, start_row)
        self._legal_moves = []

    def make_move(self, board, game, start_col, start_row, end_col, end_row):
        """passes move to parent object for testing"""
        return super().make_move(board, game, start_col, start_row, end_col, end_row)

    def set_legal_moves(self, game):
        """clear and creates a list of possible moves for the object"""
        del self._legal_moves[:]

        if self._color == "red":
            self._legal_moves.append([0,2])
            self._legal_moves.append([2,0])
            self._legal_moves.append([4,2])
            self._legal_moves.append([2,4])
            self._legal_moves.append([0,7])
            self._legal_moves.append([2,8])
            self._legal_moves.append([4,6])

        if self._color == "black":
            self._legal_moves.append([9,2])
            self._legal_moves.append([7,0])
            self._legal_moves.append([5,2])
            self._legal_moves.append([7,4])
            self._legal_moves.append([9,7])
            self._legal_moves.append([7,8])
            self._legal_moves.append([5,6])

        for i in game.get_all_pieces():
            if self.get_color == i.get_color:
                if i.get_coords in self._legal_moves:
                    self._legal_moves.remove(i.get_coords)


class Rook(Regiment):
    """
    Child of Pieces class, contains special rules pertaining to the piece
    """

    def __init__(self, team_color, name, board_label, start_col, start_row):
        """ creates object for a movie based on stated parameters """
        super().__init__(team_color, name, board_label, start_col, start_row)
        self._legal_moves = []

    def make_move(self, board, game, start_col, start_row, end_col, end_row):
        """passes move to parent object for testing"""
        return super().make_move(board, game, start_col, start_row, end_col, end_row)

    def set_legal_moves(self, game):
        """clear and creates a list of possible moves for the object"""
        del self._legal_moves[:]

        for i in range (0,11):
            self._legal_moves.append([i, self._start_row])

        for i in range (0,10):
            self._legal_moves.append([self._start_col, i])

        self._legal_moves.remove(self.get_coords()) #removes current position

        for i in game.get_all_pieces():
            if self.get_color == i.get_color:
                if i.get_coords in self._legal_moves:
                    self._legal_moves.remove(i.get_coords)

class Cannon(Regiment):
    """
    Child of Pieces class, contains special rules pertaining to the piece
    """

    def __init__(self, team_color, name, board_label, start_col, start_row):
        """ creates object for a movie based on stated parameters """
        super().__init__(team_color, name, board_label, start_col, start_row)
        self._legal_moves = []

    def make_move(self, board, game, start_col, start_row, end_col, end_row):
        """passes move to parent object for testing"""
        return super().make_move(board, game, start_col, start_row, end_col, end_row)

    def set_legal_moves(self, game):
        """clear and creates a list of possible moves for the object"""
        del self._legal_moves[:]

        for i in range(0, 11):
            self._legal_moves.append([i, self._start_row])

        for i in range(0, 10):
            self._legal_moves.append([self._start_col, i])

class Advisor(Regiment):
    """
    child of Pieces class, contains special rules pertaining to the piece
    """

    def __init__(self, team_color, name, board_label, start_col, start_row):
        """ creates object for a movie based on stated parameters """
        super().__init__(team_color, name, board_label, start_col, start_row)
        self._legal_moves = [] #holds list of pairings of possible moves where teammates are not located

    def make_move(self, board, game, start_col, start_row, end_col, end_row):
        """passes move to parent object for testing"""
        return super().make_move(board, game, start_col, start_row, end_col, end_row)

    def set_legal_moves(self, game):
        """clear and creates a list of possible moves for the object"""
        del self._legal_moves[:]

        #red team advisor
        if self.get_coords == [3, 0]:
            self._legal_moves.append([4, 1])
        if self.get_coords == [3, 2]:
            self._legal_moves.append([4, 1])
        if self.get_coords == [5, 0]:
            self._legal_moves.append([4, 1])
        if self.get_coords == [5, 2]:
            self._legal_moves.append([4, 1])
        if self.get_coords == [4, 1]:
            self._legal_moves.append([3, 0])
            self._legal_moves.append([3, 2])
            self._legal_moves.append([5, 0])
            self._legal_moves.append([5, 2])

        #black team advisor
        if self.get_coords == [4, 9]:
            self._legal_moves.append([5, 8])
        if self.get_coords == [6, 9]:
            self._legal_moves.append([5, 8])
        if self.get_coords == [4, 7]:
            self._legal_moves.append([5, 8])
        if self.get_coords == [6, 7]:
            self._legal_moves.append([5, 8])
        if self.get_coords == [5, 8]:
            self._legal_moves.append([3, 0])
            self._legal_moves.append([3, 2])
            self._legal_moves.append([5, 0])
            self._legal_moves.append([5, 2])

        for i in game.get_all_pieces():
            if self.get_color == i.get_color:
                if i.get_coords in self._legal_moves:
                    self._legal_moves.remove(i.get_coords)

class General(Regiment):
    """
    child of Pieces class, contains special rules pertaining to the piece
    """

    def __init__(self, team_color, name, board_label, start_col, start_row):
        """ creates object for a movie based on stated parameters """
        super().__init__(team_color, name, board_label, start_col, start_row)
        self._legal_moves = []

    def make_move(self, board, game, start_col, start_row, end_col, end_row):
        """passes move to parent object for testing"""
        return super().make_move(board, game, start_col, start_row, end_col, end_row)

    def get_legal_moves(self):
        return self._legal_moves

    def set_legal_moves(self, game):
        """clear and creates a list of possible moves for the object"""
        del self._legal_moves[:]

        #red team general
        if self.get_coords == [3, 0]:
            self._legal_moves.append([4, 0])
            self._legal_moves.append([3, 1])
        if self.get_coords == [4, 0]:
            self._legal_moves.append([3, 0])
            self._legal_moves.append([5, 0])
            self._legal_moves.append([4, 1])
        if self.get_coords == [5, 0]:
            self._legal_moves.append([4, 0])
            self._legal_moves.append([5, 1])
        if self.get_coords == [3, 1]:
            self._legal_moves.append([3, 2])
            self._legal_moves.append([3, 0])
            self._legal_moves.append([4, 1])
        if self.get_coords == [4, 1]:
            self._legal_moves.append([4, 0])
            self._legal_moves.append([4, 2])
            self._legal_moves.append([3, 1])
            self._legal_moves.append([5, 1])
        if self.get_coords == [5, 1]:
            self._legal_moves.append([5, 0])
            self._legal_moves.append([5, 2])
            self._legal_moves.append([4, 1])
        if self.get_coords == [3, 2]:
            self._legal_moves.append([4, 2])
            self._legal_moves.append([3, 1])
        if self.get_coords == [4, 2]:
            self._legal_moves.append([4, 1])
            self._legal_moves.append([5, 2])
            self._legal_moves.append([3, 2])
        if self.get_coords == [5, 2]:
            self._legal_moves.append([4, 2])
            self._legal_moves.append([5, 1])

        for i in game.get_all_pieces():
            if self.get_color == i.get_color:
                if i.get_coords in self._legal_moves:
                    self._legal_moves.remove(i.get_coords)


