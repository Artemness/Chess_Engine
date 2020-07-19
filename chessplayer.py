import torch
from state import State
from train import Net
import chess

class valuation(object):
    def __init__(self):
        vals = torch.load("nets/value.pth", map_location=lambda storage, loc: storage)
        self.model = Net()
        self.model.load_state_dict(vals)

    def __call__(self, s):
        npz = s.serialize()[None]
        output = self.model(torch.tensor(npz).float())
        return float(output.data[0][0])

def explore_leaves(s, e):
    ret = []
    for m in s.edges():
        s.board.push(m)
        ret.append((e(s), m))
        s.board.pop()
    return ret

if __name__ == "__main__":
    e = valuation()
    s = State()
    print(e(s))
    while not s.board.is_game_over():
        l = sorted(explore_leaves(s,e), key = lambda x: x[0], reverse=s.board.turn)
        move = l[0]
        print(move)
        s.board.push(move[1])
    print(s.board.result())