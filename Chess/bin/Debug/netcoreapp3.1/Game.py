from Board import Board


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

        if 50 < pos_y < 450 and 0 < pos_x < 400:
            pos_y -= 50

            pos_x, pos_y = pos_x // 50, pos_y // 50

            if self.is_figure_selected:
                if self.board[pos_y][pos_x].check_figure() is False or self.board[pos_y][pos_x].check_figure() \
                        and self.board[pos_y][pos_x].figure.color != self.selected_figure.color:

                    cords = (pos_y, pos_x)
                    if cords in self.selected_figure.move_options or cords in self.selected_figure.attack_options:
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

                    figure.move_options = figure.get_move_options(self.board)
                    figure.attack_options = figure.get_attack_options(self.board)
                    self.board_obj.highlight_options(figure.move_options, figure.attack_options)

    def change_turn(self):
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"

    def get_board(self):
        return self.board

    def test(self, x, y):
        self.set_pos_x(x)
        self.set_pos_y(y)
        self.process_action()


a = Game()

a.test(25, 125)
a.test(25, 225)
a.test(75, 375)
a.test(75, 275)
a.test(125, 125)
a.test(125, 175)
a.test(75, 275)
a.test(75, 225)
a.test(175, 125)
a.test(175, 175)
a.test(75, 225)

print(2 - (-1))
