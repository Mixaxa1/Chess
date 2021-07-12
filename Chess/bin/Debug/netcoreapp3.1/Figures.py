class Figure(object):
    def __init__(self, cords, color):
        self.cords = cords
        self.color = color
        self.action_options = []


class King(Figure):
    def __init__(self, cords, color, sprite=None):
        super(King, self).__init__(cords, color)

        self.sprite = "king_" + color
        self.didnt_move = True

    def get_action_options(self, board_obj):
        board_obj.get_tiles_under_attack(self.color)

        move_options = self.get_move_options(board_obj)
        attack_options = self.get_attack_options(board_obj)

        return [move_options, attack_options]

    def get_move_options(self, board_obj):
        y, x = self.cords
        board = board_obj.board
        move_options = []
        raw_options = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        for cords in raw_options:
            new_y, new_x = y + cords[0], x + cords[1]
            if new_y in range(0, 8) and new_x in range(0, 8):
                target_tile = board[new_y][new_x]
                if not target_tile.check_figure() and (new_y, new_x) not in board_obj.tiles_under_attack:
                    move_options.append((new_y, new_x))

        return move_options

    def get_attack_options(self, board_obj):
        y, x = self.cords
        board = board_obj.board
        attack_options = []
        raw_options = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        for cords in raw_options:
            new_y, new_x = y + cords[0], x + cords[1]
            if new_y in range(0, 8) and new_x in range(0, 8):
                target_tile = board[new_y][new_x]
                if target_tile.check_figure() and target_tile.figure.color != self.color \
                        and (new_y, new_x) not in board_obj.tiles_under_attack:
                    attack_options.append((new_y, new_x))

        return attack_options


class Queen(Figure):
    def __init__(self, cords, color, sprite=None):
        super(Queen, self).__init__(cords, color)

        self.sprite = "queen_" + color

    def get_action_options(self, board_obj):
        move_options = self.get_move_options(board_obj)
        attack_options = self.get_attack_options(board_obj)

        return [move_options, attack_options]

    def get_move_options(self, board_obj):
        y, x = self.cords
        board = board_obj.board
        move_options = []
        raw_options = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        for cords in raw_options:
            new_y, new_x = y + cords[0], x + cords[1]
            while new_y in range(0, 8) and new_x in range(0, 8):
                target_tile = board[new_y][new_x]
                if target_tile.check_figure() is False:
                    move_options.append((new_y, new_x))

                    new_y, new_x = new_y + cords[0], new_x + cords[1]
                else:
                    break

        return move_options

    def get_attack_options(self, board_obj):
        y, x = self.cords
        board = board_obj.board
        attack_options = []
        raw_options = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        for cords in raw_options:
            new_y, new_x = y + cords[0], x + cords[1]
            while new_y in range(0, 8) and new_x in range(0, 8):
                target_tile = board[new_y][new_x]
                if target_tile.check_figure() and target_tile.figure.color != self.color:
                    attack_options.append((new_y, new_x))
                    break
                elif target_tile.check_figure() and target_tile.figure.color == self.color:
                    break

                new_y, new_x = new_y + cords[0], new_x + cords[1]

        return attack_options


class Bishop(Figure):
    def __init__(self, cords, color, sprite=None):
        super(Bishop, self).__init__(cords, color)

        self.sprite = "bishop_" + color

    def get_action_options(self, board_obj):
        move_options = self.get_move_options(board_obj)
        attack_options = self.get_attack_options(board_obj)

        return [move_options, attack_options]

    def get_move_options(self, board_obj):
        y, x = self.cords
        board = board_obj.board
        move_options = []
        raw_options = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        for cords in raw_options:
            new_y, new_x = y + cords[0], x + cords[1]
            while new_y in range(0, 8) and new_x in range(0, 8):
                target_tile = board[new_y][new_x]
                if target_tile.check_figure() is False:
                    move_options.append((new_y, new_x))

                    new_y, new_x = new_y + cords[0], new_x + cords[1]
                else:
                    break

        return move_options

    def get_attack_options(self, board_obj):
        y, x = self.cords
        board = board_obj.board
        attack_options = []
        raw_options = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        for cords in raw_options:
            new_y, new_x = y + cords[0], x + cords[1]
            while new_y in range(0, 8) and new_x in range(0, 8):
                target_tile = board[new_y][new_x]
                if target_tile.check_figure() and target_tile.figure.color != self.color:
                    attack_options.append((new_y, new_x))
                    break
                elif target_tile.check_figure() and target_tile.figure.color == self.color:
                    break

                new_y, new_x = new_y + cords[0], new_x + cords[1]

        return attack_options


class Knight(Figure):
    def __init__(self, cords, color, sprite=None):
        super(Knight, self).__init__(cords, color)

        self.sprite = "knight_" + color

    def get_action_options(self, board_obj):
        move_options = self.get_move_options(board_obj)
        attack_options = self.get_attack_options(board_obj)

        return [move_options, attack_options]

    def get_move_options(self, board_obj):
        y, x = self.cords
        board = board_obj.board
        move_options = []
        raw_options = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        for cords in raw_options:
            new_y, new_x = y + cords[0], x + cords[1]
            if new_y in range(0, 8) and new_x in range(0, 8) and board[new_y][new_x].check_figure() is False:
                move_options.append((new_y, new_x))

        return move_options

    def get_attack_options(self, board_obj):
        y, x = self.cords
        board = board_obj.board
        attack_options = []
        raw_options = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        for cords in raw_options:
            new_y, new_x = y + cords[0], x + cords[1]
            if new_y in range(0, 8) and new_x in range(0, 8) and board[new_y][new_x].check_figure() \
                    and board[new_y][new_x].figure.color != self.color:
                attack_options.append((new_y, new_x))

        return attack_options


class Rook(Figure):
    def __init__(self, cords, color, sprite=None):
        super(Rook, self).__init__(cords, color)

        self.sprite = "rook_" + color
        self.didnt_move = True

    def get_action_options(self, board_obj):
        board_obj.get_tiles_under_attack(self.color)

        move_options = self.get_move_options(board_obj)
        castling_option = self.get_castling_option(board_obj)
        if castling_option != ():
            move_options.append(castling_option)
        attack_options = self.get_attack_options(board_obj)

        return [move_options, attack_options]

    def get_move_options(self, board_obj):
        y, x = self.cords
        board = board_obj.board
        move_options = []

        if y < 7:
            for i in range(y + 1, 8):
                if board[i][x].check_figure() is False:
                    move_options.append((i, x))
                else:
                    break
        if y > 0:
            for i in range(y - 1, -1, -1):
                if board[i][x].check_figure() is False:
                    move_options.append((i, x))
                else:
                    break
        if x < 7:
            for i in range(x + 1, 8):
                if board[y][i].check_figure() is False:
                    move_options.append((y, i))
                else:
                    break
        if x > 0:
            for i in range(x - 1, -1, -1):
                if board[y][i].check_figure() is False:
                    move_options.append((y, i))
                else:
                    break

        return move_options

    def get_castling_option(self, board_obj):
        y, x = self.cords
        board = board_obj.board
        castle_option = ()

        if x < 7:
            for i in range(x + 1, 8):
                if board[y][i].check_figure():
                    if type(board[y][i].figure) is King and board[y][i].figure.color == self.color \
                            and board[y][i].figure.didnt_move and self.didnt_move:
                        if (y, i) in board_obj.tiles_under_attack:
                            if (y, i - 1) not in board_obj.tiles_under_attack \
                                    and (y, i - 2) not in board_obj.tiles_under_attack:
                                castle_option = (y, i)
                                break
                            else:
                                break
                        else:
                            castle_option = (y, i)
                            break
                    else:
                        break

        if x > 0:
            for i in range(x - 1, -1, -1):
                if board[y][i].check_figure():
                    if type(board[y][i].figure) is King and board[y][i].figure.color == self.color \
                            and board[y][i].figure.didnt_move and self.didnt_move:
                        if (y, i) in board_obj.tiles_under_attack:
                            if (y, i + 1) not in board_obj.tiles_under_attack \
                                    and (y, i + 2) not in board_obj.tiles_under_attack:
                                castle_option = (y, i)
                                break
                            else:
                                break
                        else:
                            castle_option = (y, i)
                            break
                    else:
                        break

        return castle_option

    def get_attack_options(self, board_obj):
        y, x = self.cords
        board = board_obj.board
        attack_options = []

        if y < 7:
            for i in range(y + 1, 8):
                if board[i][x].check_figure():
                    if board[i][x].figure.color != self.color:
                        attack_options.append((i, x))
                        break
                    else:
                        break
        if y > 0:
            for i in range(y - 1, -1, -1):
                if board[i][x].check_figure():
                    if board[i][x].figure.color != self.color:
                        attack_options.append((i, x))
                        break
                    else:
                        break
        if x < 7:
            for i in range(x + 1, 8):
                if board[y][i].check_figure():
                    if board[y][i].figure.color != self.color:
                        attack_options.append((y, i))
                        break
                    else:
                        break
        if x > 0:
            for i in range(x - 1, -1, -1):
                if board[y][i].check_figure():
                    if board[y][i].figure.color != self.color:
                        attack_options.append((y, i))
                        break
                    else:
                        break

        return attack_options


class Pawn(Figure):
    def __init__(self, cords, color, sprite=None):
        super(Pawn, self).__init__(cords, color)

        self.sprite = "pawn_" + color
        self.dash_used = False

    def get_action_options(self, board_obj):
        move_options = self.get_move_options(board_obj)
        attack_options = self.get_attack_options(board_obj)

        return [move_options, attack_options]

    def get_move_options(self, board_obj):
        y, x = self.cords
        board = board_obj.board
        move_options = []

        if y not in [0, 7]:
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

        return move_options

    def get_attack_options(self, board_obj):
        y, x = self.cords
        board = board_obj.board
        attack_options = []

        if y not in [0, 7]:
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
                            attack_options.append((y - 1, x - 1)),

        return attack_options
