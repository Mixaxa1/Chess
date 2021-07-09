from Board import Board


class Game(object):
    def __init__(self):
        self.board = Board()
        self.board.generate_board()

        self.turn = "white"
        self.figure_selected = False
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

            if self.figure_selected and self.board.check_figure((pos_y, pos_x)) is False:
                move_options = self.selected_figure.get_move_options(self.board)
                if (pos_y, pos_x) in move_options:
                    self.board.move_figure(self.selected_figure.cords, (pos_x, pos_y))

            elif self.board.check_figure((pos_y, pos_x)):
                figure = self.board.board[pos_y][pos_x].figure
                if figure.color == self.turn and self.selected_figure != figure:
                    self.board.delete_highlight()

                    self.figure_selected = True
                    self.selected_figure = figure

                    move_options = figure.get_move_options(self.board)
                    attack_options = figure.get_attack_options(self.board)
                    self.board.highlight_options(move_options, attack_options)

    def get_board(self):
        return self.board.board


a = Game()

a.set_pos_x(25)
a.set_pos_y(125)
a.process_action()

a.set_pos_x(25)
a.set_pos_y(225)
a.process_action()

print 1
