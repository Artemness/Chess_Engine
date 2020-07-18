import chess
class State():
    def __init__(self):
        self.board = chess.Board()

    def serialize(self):
        pass

    def edges(self):
        return list(self.board.generate_legal_moves())

    def value(self):
        #ToDO: add neural net here
        return 1

if __name__ == "__main__":
    s = State()
    print(s.edges())