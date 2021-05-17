import math
import time
import random


class TicTacToe:
    def __init__(self):                                             #metoda inicjalizacyjna
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod                                                   #metoda statyczna, parametr self nie jest tu potrzebny
    def make_board():
        return [' ' for _ in range(9)]                              #stworzenie planszy i wypełnienie jej pustymi polami

    def print_board(self):                                          #funcja rysowania planszy, 3 rzedy i ich 'wydrukowanie'
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod                                                   #numeracja pol planszy, metoda statyczna, parametr self nie jest tu potrzebny
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):                            #funkcja ruchu gracza, square - przestrzen od 0-8, letter - litera 0 lub X
        if self.board[square] == ' ':                               #jesli przestrzen jest pusta
            self.board[square] = letter                             #przypisuję do niej litere
            if self.winner(square, letter):                         #sprawdzam czy w kwadraciku jest wygrywająca litera
                self.current_winner = letter                        #jesli tak, to zwyciezca jest uzytkownik tej litery
            return True
        return False

    def winner(self, square, letter):                               # funkcja wygranej
        row_ind = math.floor(square / 3)                           #spelnienie warunków poziomych
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):                         #jesli kazda 'litera' w rzedzie jest tą samę, zwracam TRUE
            return True
        col_ind = square % 3                                        #spelnienie warunków poziomych
        column = [self.board[col_ind+i*3] for i in range(3)]        #analogicznie jak w poziomie
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:                                          # pola parzyste ( numerowane są od 0 ), modulo / 2 z reszta 0
            diagonal1 = [self.board[i] for i in [0, 4, 8]]           #spelnienie warunku skośnego nr 1
            if all([s == letter for s in diagonal1]):                 #analogicznie jak poziom i pion
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]            #spelnienie warunku skośnego nr 2
            if all([s == letter for s in diagonal2]):                   #analogicznie jak poziom i pion
                return True
        return False

    def empty_squares(self):                                            #funkcja sprawdza, czy są jeszcze puste pola (kwadraty ) na planszy
        return ' ' in self.board

    def num_empty_squares(self):                                        # funkcja liczy puste pola ( kwadraty ) na polu
        return self.board.count(' ')

    def available_moves(self):                                          # funkcja mozliwych ruchow, zwraca wartosc numeryczna
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):    #funkcja wlasciwej rozgrywki, przyjmuje wartosc 'gra', dwojki graczy oraz wartosc true albo false jesli nie chemy drukowac planszy gry

    if print_game:
        game.print_board_nums()      # jesli w/w wartosc ma parametr true, drukujemy stany gry

    letter = 'X'                      # przypisanie wartosci
    while game.empty_squares():         # jesli plansza jest pusta to: ...
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
                return letter                                    # koniec petli, koniec gry
            letter = 'O' if letter == 'X' else 'X'               # zmiana gracza

        time.sleep(.9)                                            #opcjonalne opóźnienie wykonanie poleceń, tutaj 0.9 sekundy

    if print_game:
        print('It\'s a tie!')


class Player:             #klasa 'gracz', mozna ją wyimportować do oddzielnego pliku, a następnie importować plik klasy 'gracz',  jak moduł
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')  #za kazdym dozwolony ruchem nastepuje przyjecie - inputu
            try:
                val = int(square)                                           #zmiana przyjetej wartosci na integer
                if val not in game.available_moves():                       # jesli wartosc nie wystepuje w liscie dozwolonych ruchow
                    raise ValueError                                        # podnosze ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')                         # wiadomosc o bledzie ValueError
        return val                                                             #jesli wartosc poprawna, zwracam ją


class RandomComputerPlayer(Player):                             #klasa randomowego AI
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):                                   #funckja ruchu
        square = random.choice(game.available_moves())          # randomowe wybory ruchow z listy dozwolonych ruchow
        return square


class SmartComputerPlayer(Player):                              #  klasa 'smart" AI
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:                    # poczatkowa faza gry: jesli mozliwe jest 9 ruchow, to :
            square = random.choice(game.available_moves())      # pierwszy jest randomowy
        else:
            square = self.minimax(game, self.letter)['position']    # w innym wypadku uzywany jest algorytm minmax
        return square

    def minimax(self, state, player):                             #algorytm minmax, zwracam aktualny stan gry, gracza ktory wykonuje nastepny ruch
        max_player = self.letter                                    #max_player to gracz ludzki
        other_player = 'O' if player == 'X' else 'X'                 #wybor X lub 0
        if state.current_winner == other_player:                       #jesli obecny wygrwający to other player
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (    #zwracam wartosc NONE - pozniej nadpisana
                        state.num_empty_squares() + 1)}                 # wykorzystanie funkcji empty_squares, w zaleznosci czy jest przydatna
        elif not state.empty_squares():                                 #gdy nie ma wolnych pol
            return {'position': None, 'score': 0}                       #zwracam wynik - score : 0

        if player == max_player:                                        # jesli gracz to max_player
            best = {'position': None, 'score': -math.inf}                # kazdy wynik powinien maksymalizowac
        else:
            best = {'position': None, 'score': math.inf}                 # kazdy wynik powinien minimalizowac
        for possible_move in state.available_moves():                       #petla for dla mozliwych ruchow
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move                       # symulacja gry po wykonaniu mozliwego ruchu

            if player == max_player:                                     # jesli gracz to max_player
                if sim_score['score'] > best['score']:                     #symulacja wyniku
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best


if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')                          #smart komputer uzywa znaku x
    #x_player = RandomComputerPlayer('X')                        # wywołac mozna tylko jedno AI, w razie potrzeby moge uzyc gracza random AI
    o_player = HumanPlayer('O')                                  #gracz ludzki uzywa znaku o
    t = TicTacToe()                                              #stworzenie obiektu
    play(t, x_player, o_player, print_game=True)                 #wywołanie funkcji play