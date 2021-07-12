from Board import Board, King


class Game(object):
    def __init__(self):
        self.board_obj = Board()
        self.board_obj.generate_board()
        self.board = self.board_obj.board

        self.turn = "white"
        self.is_figure_selected = False
        self.selected_figure = None

        self.pos_x = 0
        self.pos_y = 0

    def set_pos_x(self, pos):
        self.pos_x = pos

    def set_pos_y(self, pos):
        self.pos_y = pos

    def process_action(self):
        pos_x, pos_y = self.pos_x, self.pos_y

        if 50 < pos_y <= 450 and 0 < pos_x <= 400:
            pos_y -= 50

            pos_x, pos_y = pos_x // 50, pos_y // 50

            if self.is_figure_selected:
                target_tile = self.board[pos_y][pos_x]
                if target_tile.check_figure() is False \
                        or target_tile.check_figure() and target_tile.figure.color != self.selected_figure.color \
                        or type(target_tile.figure) is King and target_tile.figure.color == self.selected_figure.color:

                    cords = (pos_y, pos_x)
                    if cords in self.selected_figure.action_options[0] \
                            or cords in self.selected_figure.action_options[1]:
                        self.board_obj.move_figure(self.selected_figure.cords, (pos_y, pos_x))

                        self.change_turn()

                self.board_obj.delete_highlight()
                self.is_figure_selected = False
                self.selected_figure = None

            elif self.board[pos_y][pos_x].check_figure():
                figure = self.board[pos_y][pos_x].figure
                if figure.color == self.turn and self.selected_figure != figure:
                    self.board_obj.delete_highlight()

                    self.is_figure_selected = True
                    self.selected_figure = figure

                    figure.action_options = figure.get_action_options(self.board_obj)
                    self.board_obj.highlight_options(figure.action_options)

    def change_turn(self):
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"

    def get_turn(self):
        return self.turn

    def get_board(self):
        return self.board

    def test(self, x, y):
        self.set_pos_x(50 * x - 25)
        self.set_pos_y(50 * y + 50 - 25)
        self.process_action()


a = Game()

a.test(7, 2)
a.test(7, 3)

a.test(1, 7)
a.test(1, 6)

a.test(6, 1)
a.test(8, 3)

a.test(1, 6)
a.test(1, 5)

a.test(8, 3)
a.test(7, 4)

print(a.board[5][5].figure)
