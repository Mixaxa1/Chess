from Board import Board


class Game(object):
    def __init__(self):
        self.board = Board()
        self.board.generate_board()

        self.turn = "white"
        self.figure_selected = False
        self.pos_x = 0
        self.pos_y = 0

    def set_pos_x(self, pos):
        self.pos_x = pos

    def set_pos_y(self, pos):
        self.pos_y = pos

    def process_action(self):
        if self.figure_selected is False:
            self.board.delete_highlight()

        if 50 < self.pos_y < 450 and 0 < self.pos_x < 400:
            self.pos_y -= 50

            self.pos_x, self.pos_y = self.pos_x // 50, self.pos_y // 50

            if self.board.check_figure((self.pos_y, self.pos_x)):
                figure = self.board.board[self.pos_y][self.pos_x].figure
                if figure.color == self.turn:
                    self.figure_selected = True

                    move_options = figure.get_move_options(self.board)
                    attack_options = figure.get_attack_options(self.board)
                    self.board.highlight_options(move_options, attack_options)

    def get_board(self):
        return self.board.board


a = Game()
