class Figure(object):
    def __init__(self, cords, color):
        self.cords = cords
        self.color = color

        self.move_options = []
        self.attack_options = []


class King(Figure):
    def __init__(self, cords, color, sprite=None):
        super(King, self).__init__(cords, color)

        self.sprite = "king_" + color

    def check_move(self):
        pass


class Queen(Figure):
    def __init__(self, cords, color, sprite=None):
        super(Queen, self).__init__(cords, color)

        self.sprite = "queen_" + color

    def check_move(self):
        pass


class Bishop(Figure):
    def __init__(self, cords, color, sprite=None):
        super(Bishop, self).__init__(cords, color)

        self.sprite = "bishop_" + color

    def check_move(self):
        pass


class Knight(Figure):
    def __init__(self, cords, color, sprite=None):
        super(Knight, self).__init__(cords, color)

        self.sprite = "knight_" + color

    def check_move(self):
        pass


class Rook(Figure):
    def __init__(self, cords, color, sprite=None):
        super(Rook, self).__init__(cords, color)

        self.sprite = "rook_" + color

    def get_move_options(self, board):
        y, x = self.cords
        options = []

        return options

    def get_attack_options(self, board):
        y, x = self.cords
        field = board.board
        options = []

        return options


class Pawn(Figure):
    def __init__(self, cords, color, sprite=None):
        super(Pawn, self).__init__(cords, color)

        self.sprite = "pawn_" + color
        self.dash_used = False

    def get_move_options(self, board):
        y, x = self.cords
        options = []

        if y not in [0, 7]:
            if self.color == "white":
                if board[y + 1][x].check_figure() is False:
                    options.append((y + 1, x))
                    if board[y + 2][x].check_figure() is False and y == 1:
                        options.append((y + 2, x))

            elif self.color == "black":
                if board[y - 1][x].check_figure() is False:
                    options.append((y - 1, x))
                    if board[y - 2][x].check_figure() is False and y == 6:
                        options.append((y - 2, x))

        return options

    def get_attack_options(self, board):
        y, x = self.cords
        options = []

        if y not in [0, 7]:
            if self.color == "white":
                if 0 <= x < 7:
                    if board[y + 1][x + 1].check_figure():
                        if board[y + 1][x + 1].figure.color != self.color:
                            options.append((y + 1, x + 1))

                    if board[y][x + 1].check_figure() and board[y + 1][x + 1].check_figure() is False:
                        if type(board[y][x + 1].figure) is Pawn and board[y][x + 1].figure.color != self.color \
                                and board[y][x + 1].figure.dash_used is True and y == 5:
                            options.append((y + 1, x + 1))

                if 0 < x <= 7:
                    if board[y + 1][x - 1].check_figure():
                        if board[y + 1][x - 1].figure.color != self.color:
                            options.append((y + 1, x - 1))

                    if board[y][x - 1].check_figure() and board[y + 1][x - 1].check_figure() is False:
                        if type(board[y][x - 1].figure) is Pawn and board[y][x - 1].figure.color != self.color\
                                and board[y][x - 1].figure.dash_used is True and y == 5:
                            options.append((y + 1, x - 1))

            if self.color == "black":
                if 0 <= x < 7:
                    if board[y - 1][x + 1].check_figure():
                        if board[y - 1][x + 1].figure.color != self.color:
                            options.append((y - 1, x + 1))

                    if board[y][x + 1].check_figure() and board[y - 1][x + 1].check_figure() is False:
                        if type(board[y][x + 1].figure) is Pawn and board[y][x + 1].figure.color != self.color\
                                and board[y][x + 1].figure.dash_used is True and y == 3:
                            options.append((y - 1, x + 1))

                if 0 < x <= 7:
                    if board[y - 1][x - 1].check_figure():
                        if board[y - 1][x - 1].figure.color != self.color:
                            options.append((y - 1, x - 1))

                    if board[y][x - 1].check_figure() and board[y - 1][x - 1].check_figure() is False:
                        if type(board[y][x - 1].figure) is Pawn and board[y][x - 1].figure.color != self.color \
                                and board[y][x - 1].figure.dash_used is True and y == 3:
                            options.append((y - 1, x - 1))

        return options
