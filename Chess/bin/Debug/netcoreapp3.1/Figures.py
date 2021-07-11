class Figure(object):
    def __init__(self, cords, color):
        self.cords = cords
        self.color = color
        self.action_options = []


class King(Figure):
    def __init__(self, cords, color, sprite=None):
        super(King, self).__init__(cords, color)

        self.sprite = "king_" + color

    def get_action_options(self, board):
        y, x = self.cords
        move_options = []
        attack_options = []

        return [move_options, attack_options]


class Queen(Figure):
    def __init__(self, cords, color, sprite=None):
        super(Queen, self).__init__(cords, color)

        self.sprite = "queen_" + color

    def get_action_options(self, board):
        y, x = self.cords
        move_options = []
        attack_options = []

        return [move_options, attack_options]


class Bishop(Figure):
    def __init__(self, cords, color, sprite=None):
        super(Bishop, self).__init__(cords, color)

        self.sprite = "bishop_" + color

    def get_action_options(self, board):
        y, x = self.cords
        move_options = []
        attack_options = []

        return [move_options, attack_options]


class Knight(Figure):
    def __init__(self, cords, color, sprite=None):
        super(Knight, self).__init__(cords, color)

        self.sprite = "knight_" + color

    def get_action_options(self, board):
        y, x = self.cords
        move_options = []
        attack_options = []

        return [move_options, attack_options]


class Rook(Figure):
    def __init__(self, cords, color, sprite=None):
        super(Rook, self).__init__(cords, color)

        self.sprite = "rook_" + color

    def get_action_options(self, board):
        y, x = self.cords
        move_options = []
        attack_options = []

        return [move_options, attack_options]


class Pawn(Figure):
    def __init__(self, cords, color, sprite=None):
        super(Pawn, self).__init__(cords, color)

        self.sprite = "pawn_" + color
        self.dash_used = False

    def get_action_options(self, board):
        y, x = self.cords

        if y not in [0, 7]:
            move_options = []

            if self.color == "white":
                if board[y + 1][x].check_figure() is False:
                    move_options.append((y + 1, x))
                    if board[y + 2][x].check_figure() is False and y == 1:
                        move_options.append((y + 2, x))

            elif self.color == "black":
                if board[y - 1][x].check_figure() is False:
                    move_options.append((y - 1, x))
                    if board[y - 2][x].check_figure() is False and y == 6:
                        move_options.append((y - 2, x))

            attack_options = []

            if self.color == "white":
                if 0 <= x < 7:
                    if board[y + 1][x + 1].check_figure():
                        if board[y + 1][x + 1].figure.color != self.color:
                            attack_options.append((y + 1, x + 1))

                    if board[y][x + 1].check_figure() and board[y + 1][x + 1].check_figure() is False:
                        if type(board[y][x + 1].figure) is Pawn and board[y][x + 1].figure.color != self.color \
                                and board[y][x + 1].figure.dash_used is True and y == 4:
                            attack_options.append((y + 1, x + 1))

                if 0 < x <= 7:
                    if board[y + 1][x - 1].check_figure():
                        if board[y + 1][x - 1].figure.color != self.color:
                            attack_options.append((y + 1, x - 1))

                    if board[y][x - 1].check_figure() and board[y + 1][x - 1].check_figure() is False:
                        if type(board[y][x - 1].figure) is Pawn and board[y][x - 1].figure.color != self.color\
                                and board[y][x - 1].figure.dash_used is True and y == 4:
                            attack_options.append((y + 1, x - 1))

            if self.color == "black":
                if 0 <= x < 7:
                    if board[y - 1][x + 1].check_figure():
                        if board[y - 1][x + 1].figure.color != self.color:
                            attack_options.append((y - 1, x + 1))

                    if board[y][x + 1].check_figure() and board[y - 1][x + 1].check_figure() is False:
                        if type(board[y][x + 1].figure) is Pawn and board[y][x + 1].figure.color != self.color\
                                and board[y][x + 1].figure.dash_used is True and y == 3:
                            attack_options.append((y - 1, x + 1))

                if 0 < x <= 7:
                    if board[y - 1][x - 1].check_figure():
                        if board[y - 1][x - 1].figure.color != self.color:
                            attack_options.append((y - 1, x - 1))

                    if board[y][x - 1].check_figure() and board[y - 1][x - 1].check_figure() is False:
                        if type(board[y][x - 1].figure) is Pawn and board[y][x - 1].figure.color != self.color \
                                and board[y][x - 1].figure.dash_used is True and y == 3:
                            attack_options.append((y - 1, x - 1))

        return [move_options, attack_options]
