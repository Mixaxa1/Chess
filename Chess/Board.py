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
                self.board[i][j].append(Tile(cords, get_tile_color(cords)))

        for i in [0, 1, 6, 7]:
            for j in range(8):
                self.board[i][j].figure = get_figure((j, i))

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
    if cords[0] < 2:
        return "white"
    else:
        return "black"


def get_figure(cords):
    if cords[1] in (0, 7):
        if cords[0] in (0, 7):
            return Rook(cords, get_figure_color(cords))
        elif cords[0] in (1, 6):
            return Knight(cords, get_figure_color(cords))
        elif cords[0] in (2, 5):
            return Elefant(cords, get_figure_color(cords))
        elif cords[0] == 3:
            return Queen(cords, get_figure_color(cords))
        elif cords[0] == 4:
            return King(cords, get_figure_color(cords))
    else:
        return Pawn(cords, get_figure_color(cords))
