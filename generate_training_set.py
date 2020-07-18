import os
import chess.pgn
from state import State

def database(num_samples=None):
    X, Y = [], []
    gamenum = 0
    for fn in os.listdir('games'):
        pgn = open(os.path.join('games', fn))
        while 1:
            try:
               game = chess.pgn.read_game(pgn)
            except Exception:
                break
            gamenum += 1
            value = {'1/2-1/2':0, '0-1': -1, '1-0': 1}[game.headers['Result']]
            board = game.board()
            for i, move in enumerate(game.mainline_moves()):
                board.push(move)
                ser = State(board) .serialize()[0]
                X.append(ser)
                Y.append(value)
            print('Parsing Game Number: ' + str(gamenum) + '! Have ' + str(len(X)) + ' number of Examples')
            if num_samples is not None and len(X) > num_samples:
                return X,Y

if __name__ == '__main__':
    X,Y= database(10000)