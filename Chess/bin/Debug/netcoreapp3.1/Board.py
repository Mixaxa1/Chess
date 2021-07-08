from Figures import *


class Tile:
    def __init__(self, cords, color):
        self.cords = cords
        self.color = color
        self.figure = None


class Board:
    def __init__(self):
        self.board = [[] for i in range(8)]

    def generate_board(self):
        for i in range(8):
            for j in range(8):
                cords = (i, j)
                self.board[i].append(Tile(cords, get_tile_color(cords)))

        for i in [0, 1, 6, 7]:
            for j in range(8):
                self.board[i][j].figure = get_figure((j, i))

        return self.board

    def delete_figure(self, cords):
        self.board[cords[1]][cords[0]].figure = None

    def get_board(self):
        return self.board


def get_tile_color(cords):
    if cords[0] % 2 == 0:
        if cords[1] % 2 == 0:
            return "white"
        else:
            return "black"
    else:
        if cords[1] % 2 == 0:
            return "black"
        else:
            return "white"


def get_figure_color(cords):
    if cords[1] < 2:
        return "white"
    else:
        return "black"


def get_figure(cords):
    color = get_figure_color(cords)

    if cords[1] in (0, 7):
        if cords[0] in (0, 7):
            return Rook([cord * 50 + 4 for cord in cords], color)
        elif cords[0] in (1, 6):
            return Knight([cord * 50 + 4 for cord in cords], color)
        elif cords[0] in (2, 5):
            return Bishop([cord * 50 + 4 for cord in cords], color)
        elif cords[0] == 3:
            return Queen([cord * 50 + 4 for cord in cords], color)
        elif cords[0] == 4:
            return King([cord * 50 + 4 for cord in cords], color)
    else:
        return Pawn([cord * 50 + 4 for cord in cords], color)
