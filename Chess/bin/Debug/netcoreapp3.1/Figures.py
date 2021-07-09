class Figure(object):
    def __init__(self, cords, color):
        self.cords = cords
        self.color = color


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

    def check_move(self):
        pass


class Pawn(Figure):
    def __init__(self, cords, color, sprite=None):
        super(Pawn, self).__init__(cords, color)

        self.sprite = "pawn_" + color
        self.dash_used = False

    def get_move_options(self, board):
        x, y = self.cords
        options = []

        if y not in [0, 7]:
            if self.color == "white":
                if board.check_figure((y + 1, x)) is False:
                    options.append((y + 1, x))
                    if board.check_figure((y + 2, x)) is False and y == 1:
                        options.append((y + 2, x))

            elif self.color == "black":
                if board.check_figure((y - 1, x)) is False:
                    options.append((y - 1, x))
                    if board.check_figure((y - 2, x)) is False and y == 7:
                        options.append((y - 2, x))

        return options

    def get_attack_options(self, board):
        x, y = self.cords
        field = board.board
        options = []

        if y not in [0, 7]:
            if self.color == "white":
                if 0 <= x < 7:
                    if board.check_figure((y + 1, x + 1)):
                        if field[y + 1][x + 1].figure.color != self.color:
                            options.append((y + 1, x + 1))

                    if board.check_figure((y, x + 1)) and board.check_figure((y + 1, x + 1)) is False:
                        if type(field[y][x + 1].figure) is Pawn and field[y][x + 1].figure.color != self.color:
                            options.append((y + 1, x + 1))

                if 0 < x <= 7:
                    if board.check_figure((y + 1, x - 1)):
                        if field[y + 1][x - 1].figure.color != self.color:
                            options.append((y + 1, x - 1))

                    if board.check_figure((y, x - 1)) and board.check_figure((y + 1, x - 1)) is False:
                        if type(field[y][x - 1].figure) is Pawn and field[y][x - 1].figure.color != self.color:
                            options.append((y + 1, x - 1))

            if self.color == "black":
                if 0 <= x < 7:
                    if board.check_figure((y - 1, x + 1)):
                        if field[y - 1][x + 1].figure.color != self.color:
                            options.append((y - 1, x + 1))

                    if board.check_figure((y, x + 1)) and board.check_figure((y - 1, x + 1)) is False:
                        if type(field[y][x + 1].figure) is Pawn and field[y][x + 1].figure.color != self.color:
                            options.append((y - 1, x + 1))

                if 0 < x <= 7:
                    if board.check_figure((y - 1, x - 1)):
                        if field[y + 1][x - 1].figure.color != self.color:
                            options.append((y - 1, x - 1))

                    if board.check_figure((y, x - 1)) and board.check_figure((y - 1, x - 1)) is False:
                        if type(field[y][x - 1].figure) is Pawn and field[y][x - 1].figure.color != self.color:
                            options.append((y - 1, x - 1))

        return options
