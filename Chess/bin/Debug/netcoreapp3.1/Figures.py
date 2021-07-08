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

    def check_move(self):
        pass
