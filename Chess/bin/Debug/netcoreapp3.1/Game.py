from Board import Board


class Game(object):
    def __init__(self):
        self.board = Board()
        self.board.generate_board()

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
                if self.board.check_figure((pos_y, pos_x)) is False or self.board.check_figure((pos_y, pos_x)) \
                        and self.board.board[pos_y][pos_x].figure.color != self.selected_figure.color:

                    cords = (pos_y, pos_x)
                    if cords in self.selected_figure.move_options or cords in self.selected_figure.attack_options:
                        self.board.move_figure(self.selected_figure.cords, (pos_y, pos_x))

                        self.change_turn()

                self.board.delete_highlight()
                self.is_figure_selected = False
                self.selected_figure = None

            elif self.board.check_figure((pos_y, pos_x)):
                figure = self.board.board[pos_y][pos_x].figure
                if figure.color == self.turn and self.selected_figure != figure:
                    self.board.delete_highlight()

                    self.is_figure_selected = True
                    self.selected_figure = figure

                    figure.move_options = figure.get_move_options(self.board)
                    figure.attack_options = figure.get_attack_options(self.board)
                    self.board.highlight_options(figure.move_options, figure.attack_options)

    def change_turn(self):
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"

    def get_board(self):
        return self.board.board


a = Game()

a.set_pos_x(25)
a.set_pos_y(125)
a.process_action()

a.set_pos_x(25)
a.set_pos_y(225)
a.process_action()

a.set_pos_x(75)
a.set_pos_y(375)
a.process_action()

a.set_pos_x(75)
a.set_pos_y(275)
a.process_action()

a.set_pos_x(25)
a.set_pos_y(225)
a.process_action()

a.set_pos_x(75)
a.set_pos_y(275)
a.process_action()

print (1)
