Zero Knowledge Chess Engine

* Establish Search Tree
* Use a neural net to prune the tree

Def: Value Network
V - F(board)

State(Board):

Pieces(2+7*2 - 16):
* Universal
** Blank
** Blank (en passant)
* Pieces
* Pawn
* Bishop
* Knight
* Rook
* Rook (can castle)
* Queen
* King


extra state:
* To move

8*8X4 + 1 = 257 bits (vector of 0 or 1)