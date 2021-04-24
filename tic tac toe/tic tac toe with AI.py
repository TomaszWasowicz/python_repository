import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer                 # import modułów gracz ludzki i inteligencja typu 'smart'


class TicTacToe:
    def __init__(self):                                             #metoda inicjalizacyjna
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod                                                   #metoda statyczna, parametr self nie jest tu potrzebny
    def make_board():
        return [' ' for _ in range(9)]                              #wypełnienie planszy pustymi polami

    def print_board(self):                                          #funcja rysowania planszy
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:   #składana pętla
            print('| ' + ' | '.join(row) + ' |')                    #rysowanie planszy, rzedy oddzilone znakiem "|"

    @staticmethod                                                   #numeracja pol planszy, metoda statyczna, parametr self nie jest tu potrzebny
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]    #składana petla
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):                               # funkcja wygranej
        row_ind = math.floor(square / 3)                           #spelnienie warunków poziomych
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3                                        #spelnienie warunków poziomych
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:                                          # pola parzyste ( numerowane są od 0 ), modulo / 2 z reszta 0
            diagonal1 = [self.board[i] for i in [0, 4, 8]]           #spelnienie warunku skośnego nr 1
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]            #spelnienie warunku skośnego nr 2
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):                                #funkcja "gra"

    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter                                               # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'                          # switches player

        time.sleep(.9)                                                      #opcjonalne opóźnienie wykonanie poleceń, tutaj 0.9 sekundy

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')                          #smart komputer uzywa znaku x
    #x_player = RandomComputerPlayer('X')                           # wywołac mozna tylko jedno AI, w razie potrzeb, wywolujemy tylko obiekt randomAI
    o_player = HumanPlayer('O')                                  #gracz ludzki uzywa znaku o
    t = TicTacToe()                                              #stworzenie obiektu
    play(t, x_player, o_player, print_game=True)                 #wywołanie funkcji play