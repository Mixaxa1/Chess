from Figures import *


class Tile(object):
    def __init__(self, cords, color):
        self.cords = cords
        self.color = color
        self.figure = None
        self.highlighted = False
        self.highlight_color = "yellow"


class Board(object):
    def __init__(self):
        self.board = [[] for i in range(8)]

    def generate_board(self):
        for i in range(8):
            for j in range(8):
                cords = (j, i)
                self.board[i].append(Tile(cords, get_tile_color(cords)))

        for i in range(8):
            for j in [0, 1, 6, 7]:
                self.board[j][i].figure = get_figure((j, i))

    def highlight_options(self, move_options, attack_options):
        for cords in move_options:
            x, y = cords
            self.board[y][x].highlight_color = 'yellow'
            self.board[y][x].highlighted = True

        for cords in attack_options:
            x, y = cords
            self.board[y][x].highlight_color = 'red'
            self.board[y][x].highlighted = True

    def delete_highlight(self):
        for row in self.board:
            for tile in row:
                tile.highlighted = False

    def check_figure(self, cords):
        if self.board[cords[0]][cords[1]].figure is None:
            return False
        return True

    def move_figure(self, cords1, cords2):
        cord_y1, cord_x1 = cords1
        cord_y2, cord_x2 = cords2

        figure = self.board[cord_y1][cord_x1].figure
        figure.cords = (cord_y2, cord_x2)

        self.board[cord_y1][cord_x1].figure = None
        self.board[cord_y2][cord_x2].figure = figure

    def attack(self, cords1, cords2):
        cord_y1, cord_x1 = cords1
        cord_y2, cord_x2 = cords2

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
    color = get_figure_color(cords)

    if cords[0] in (0, 7):
        if cords[1] in (0, 7):
            return Rook(cords, color)
        elif cords[1] in (1, 6):
            return Knight(cords, color)
        elif cords[1] in (2, 5):
            return Bishop(cords, color)
        elif cords[1] == 3:
            return Queen(cords, color)
        elif cords[1] == 4:
            return King(cords, color)
    else:
        return Pawn(cords, color)

